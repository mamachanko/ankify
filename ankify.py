#!/usr/bin/env python

""" TODO """


from typing import List, Dict, Union
import genanki
import hashlib
import markdown2
import os
import re
import sys
import tempfile


class Card:
    def __init__(self, front, back):
        self.front = front
        self.back = back

    def __eq__(self, other):
        return self.front == other.front and self.back == other.back

    def render_back(self):
        return markdown2.markdown(
            self.back, extras=["tables", "cuddled-lists", "fenced-code-blocks"]
        )


class Deck:
    def __init__(self, title, cards=[]):
        self.title = title
        self.cards = cards

    def withCard(self, card: Card):
        return Deck(self.title, [*self.cards, card])

    @property
    def id(self):
        hash_func = hashlib.sha256()
        hash_func.update(self.title.encode("utf-8"))
        return int(hash_func.hexdigest(), 16) % (10 ** 16)

    def as_anki_deck(self):
        model = genanki.Model(
            self.id,
            "{} model".format(self.title),
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

        anki_deck = genanki.Deck(self.id, self.title)

        for card in self.cards:
            note = genanki.Note(model=model, fields=[card.front, card.render_back()])
            anki_deck.add_note(note)

        return anki_deck

    def save_as(self, filename):
        genanki.Package(self.as_anki_deck()).write_to_file(filename)

    def read_anki_deck(self) -> str:
        _, tmp_file = tempfile.mkstemp()
        genanki.Package(self.as_anki_deck()).write_to_file(tmp_file)
        with open(tmp_file, "rb") as file:
            return file.read()

    def __eq__(self, other):
        return self.title == other.title and self.cards == other.cards

    @staticmethod
    def from_file(filename: str):
        with open(filename, "r") as file:
            return Deck.from_doc(file.read())

    @staticmethod
    def from_doc(doc: str):
        return Deck._parse_doc(doc)

    @staticmethod
    def _parse_doc(doc: str):
        """ TODO """
        card_regex = r"^# (?P<front>[\S ]*).(?P<back>^((?!^# ).)*$)"
        title_regex = r"(?<=---).*title\s*:\s*(?P<title>[\w '-_]*$).*(?=---)"

        card_matches = re.finditer(card_regex, doc, re.MULTILINE | re.DOTALL)

        title_match = re.search(title_regex, doc, re.MULTILINE | re.DOTALL)
        if title_match:
            title = title_match["title"]
        else:
            title = ""

        cards = [Card(**card_match.groupdict()) for card_match in card_matches]

        return Deck(title, cards)


def get_basename_noext(filename: str) -> str:
    """ TODO """
    return os.path.splitext(os.path.basename(filename))[0]


def help():
    print("Usage: {} [ FILE | - ]".format(sys.argv[0]))
    sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        help()

    filename = sys.argv[1]

    if filename == "-":
        doc = sys.stdin.read()
        sys.stdout.buffer.write(Deck.from_doc(doc).read_anki_deck())
    else:
        name = get_basename_noext(filename)
        Deck.from_file(filename).save_as("{}.apkg".format(name))
