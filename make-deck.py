#!/usr/bin/env python

from typing import List, Dict
import genanki
import hashlib
import markdown2
import os
import re
import sys

def main(filename: str):
    name = get_basename_noext(filename)
    notes = parse_notes(filename)
    deck = create_deck(name, notes)
    save_deck(deck, name)

def parse_notes(filename: str)-> List[Dict[str, str]]:
    with open(filename, 'r') as f:
        title_regex = re.compile('1.\s*_(?P<title>.*)_')

        cards = []
        current = None

        for line in f.readlines():
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

        return cards

def create_deck(name: str, cards: List[Dict[str, str]]) -> genanki.Deck:
    deck_id = model_id = hash(name)
    model_name = '{} model'.format(name)

    model = genanki.Model(
        model_id,
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

    deck = genanki.Deck(deck_id, name)

    for c in cards:
        rendered_card_back = markdown2.markdown(c["body"], extras=["tables"])

        deck.add_note(
            genanki.Note(
                model=model,
                fields=[c["title"], rendered_card_back]
            )
        )

    return deck


def save_deck(deck: genanki.Deck, name: str):
    genanki.Package(deck).write_to_file('{}.apkg'.format(name))

def get_basename_noext(filename: str) -> str:
    return os.path.splitext(os.path.basename(filename))[0]

def hash(s: str) -> int:
    h = hashlib.sha256()
    h.update(s.encode('utf-8'))
    return int(h.hexdigest(), 16) % (10 ** 16)

if __name__ == "__main__":
    print(sys.argv)

    if len(sys.argv) < 2:
        print("Usage: {} FILE".format(sys.argv[0]))
        sys.exit(1)

    FILENAME=sys.argv[1]

    main(FILENAME)
