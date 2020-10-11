#!/usr/bin/env python

""" TODO """


from typing import List, Dict, Union
import hashlib
import os
import re
import sys
import genanki
import markdown2


def parse_notes(doc: str) -> List[Dict[str, Union[str, Dict[str, str]]]]:
    """ TODO """
    card_regex = r"^# (?P<front>[\S ]*).(?P<back>^((?!^# ).)*$)"
    title_regex = r"(?<=---).*title\s*:\s*(?P<title>[\w '-_]*$).*(?=---)"

    card_matches = re.finditer(card_regex, doc, re.MULTILINE | re.DOTALL)

    title_match = re.search(title_regex, doc, re.MULTILINE | re.DOTALL)
    if title_match:
        title = title_match["title"]
    else:
        title = ""

    return {
        "title": title,
        "cards": [card_match.groupdict() for card_match in card_matches],
    }


def create_anki_deck(deck) -> genanki.Deck:
    """ TODO """

    deck_id = model_id = hash_int(deck["title"])
    model_name = "{} model".format(deck["title"])

    model = genanki.Model(
        model_id,
        model_name,
        fields=[
            {"name": "Question"},
            {"name": "Answer"},
        ],
        templates=[
            {
                "name": "Card 1",
                "qfmt": "{{Question}}",
                "afmt": '{{FrontSide}}<hr id="answer">{{Answer}}',
            },
        ],
    )

    anki_deck = genanki.Deck(deck_id, deck["title"])

    for card in deck["cards"]:
        note = genanki.Note(
            model=model, fields=[card["front"], render_markdown(card["back"])]
        )
        anki_deck.add_note(note)

    return anki_deck


def save_deck(deck: genanki.Deck, name: str):
    """ TODO """
    genanki.Package(deck).write_to_file("{}.apkg".format(name))


def get_basename_noext(filename: str) -> str:
    """ TODO """
    return os.path.splitext(os.path.basename(filename))[0]


def hash_int(s: str) -> int:
    """ TODO """
    h = hashlib.sha256()
    h.update(s.encode("utf-8"))
    return int(h.hexdigest(), 16) % (10 ** 16)


def render_markdown(markdown: str) -> str:
    return markdown2.markdown(markdown, extras=["tables", "cuddled-lists", "fenced-code-blocks"])


def help():
    print("Usage: {} FILE".format(sys.argv[0]))
    sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        _help()

    filename = sys.argv[1]

    with open(filename, "r") as notes_file:
        name = get_basename_noext(filename)
        deck = parse_notes(notes_file.read())
        anki_deck = create_anki_deck(deck)
        save_deck(anki_deck, name)
