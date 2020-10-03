#!/usr/bin/env python

""" TODO """

from typing import List, Dict
import hashlib
import os
import re
import sys

import genanki
import markdown2

def parse_notes(notes: str) -> List[Dict[str, str]]:
    """ TODO """
    title_regex = re.compile(r'1.\s*_(?P<title>.*)_')

    cards = []
    current = None

    for line in notes.splitlines():
        if line.startswith('1.'):
            if current:
                cards.append(current.copy())
            current = None

            current = {
                'title': title_regex.match(line).group('title'),
                'body': ''
            }

        else:
            if current:
                current['body'] += line
    else:
        if current:
            cards.append(current.copy())

    return cards

def create_deck(deck_name: str, cards: List[Dict[str, str]]) -> genanki.Deck:
    """ TODO """
    deck_id = model_id = hash_int(deck_name)
    model_name = '{} model'.format(deck_name)

    model = genanki.Model(
        model_id,
        model_name,
        fields=[
            {'name': 'Question'},
            {'name': 'Answer'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Question}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
            },
        ]
    )

    deck = genanki.Deck(deck_id, deck_name)

    for card in cards:
        note = genanki.Note(
            model=model,
            fields=[
                card["title"],
                render_markdown(card["body"])
            ]
        )
        deck.add_note(note)

    return deck


def save_deck(deck: genanki.Deck, name: str):
    """ TODO """
    genanki.Package(deck).write_to_file('{}.apkg'.format(name))

def get_basename_noext(filename: str) -> str:
    """ TODO """
    return os.path.splitext(os.path.basename(filename))[0]

def hash_int(s: str) -> int:
    """ TODO """
    h = hashlib.sha256()
    h.update(s.encode('utf-8'))
    return int(h.hexdigest(), 16) % (10 ** 16)

def render_markdown(markdown: str) -> str:
    return markdown2.markdown(markdown, extras=["tables"])

def help():
    print("Usage: {} FILE".format(sys.argv[0]))
    sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        _help()

    filename = sys.argv[1]

    with open(filename, 'r') as notes_file:
        name = get_basename_noext(filename)
        notes = parse_notes(notes_file.read())
        deck = create_deck(name, notes)
        save_deck(deck, name)
