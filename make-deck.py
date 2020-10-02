#!/usr/bin/env python

import re
import markdown2
import genanki

title_regex = re.compile('1.\s*_(?P<title>.*)_')
lines = open('practical_vim.md', 'r').readlines()

cards = []
current = None

for l in lines:
  if l.startswith('1.'):
    if current:
      cards.append(current.copy())
      current = None

    current = {
      'title': title_regex.match(l).group('title'),
      'body': ''
    }

  else:
    if current:
        current['body'] += l

pracvim_model = genanki.Model(
  98098098098,
  'Practical Vim model',
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
  ])

pracvim_deck = genanki.Deck(
  123456987987,
  'Practical Vim'
)

for card in cards:
  title = card["title"]
  body = card["body"]

  rendered_card_back = markdown2.markdown(body, extras=["tables"])

  pracvim_card = genanki.Note(model=pracvim_model, fields=[title, rendered_card_back])
  pracvim_deck.add_note(pracvim_card)

genanki.Package(pracvim_deck).write_to_file('practical_vim.apkg')

