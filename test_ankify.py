import ankify
import inspect


def test_parses_title():
    doc = """
---
title: The deck's title
---
# Front of the card
Back of the card
"""

    got = ankify.parse_notes(doc)
    want = ankify.Deck("The deck's title").withCard(
        {
            "front": "Front of the card",
            "back": "Back of the card\n",
        }
    )

    assert got == want


def test_parses_notes_with_code():
    doc = """
# How to quit Vim

```
:q
:quit!
:wq
<S-z><S-z>
```
"""
    got = ankify.parse_notes(doc)
    want = ankify.Deck("").withCard(
        {
            "front": "How to quit Vim",
            "back": """
```
:q
:quit!
:wq
<S-z><S-z>
```
""",
        }
    )

    assert got == want


def test_parses_notes_with_subsection():
    doc = """
# A tiddly-bit of Javascript

So, Javascript is a thing.

## Some JS code

```javascript
var x = 'one'
var y = 'two'

const f = (a, b) => {
  r = a + b
  return r
}

console.log(f(x, y))
```

"""
    got = ankify.parse_notes(doc)
    want = ankify.Deck("").withCard(
        {
            "front": "A tiddly-bit of Javascript",
            "back": """
So, Javascript is a thing.

## Some JS code

```javascript
var x = 'one'
var y = 'two'

const f = (a, b) => {
  r = a + b
  return r
}

console.log(f(x, y))
```

""",
        }
    )

    assert got == want


def test_parses_notes_with_lists():
    doc = """
# Here's just some text

a list:
 * 1 one
 * 3 Sun Oct 11 09:32:49 2020
 * 5 three
 * 7

- sdfklj
- sdfklj
- sdfklj

1. sdfklj
1. sdfklj
1. sdfklj

> a interesting quote.
> - the author
"""
    got = ankify.parse_notes(doc)
    want = ankify.Deck("").withCard(
        {
            "front": "Here's just some text",
            "back": """
a list:
 * 1 one
 * 3 Sun Oct 11 09:32:49 2020
 * 5 three
 * 7

- sdfklj
- sdfklj
- sdfklj

1. sdfklj
1. sdfklj
1. sdfklj

> a interesting quote.
> - the author
""",
        }
    )

    assert got == want


def test_parses_notes_with_tables():
    doc = """
# Cool command-line tools

| Tool | What's cool |
|------|-------------|
| sed | replace things in streams of text |
| find | find files |
| awk | process files |

"""

    got = ankify.parse_notes(doc)
    want = ankify.Deck("").withCard(
        {
            "front": "Cool command-line tools",
            "back": """
| Tool | What's cool |
|------|-------------|
| sed | replace things in streams of text |
| find | find files |
| awk | process files |

""",
        }
    )

    assert got == want
