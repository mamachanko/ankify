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

    got = ankify.Deck.from_doc(doc)
    want = ankify.Deck("The deck's title").withCard(
        ankify.Card(
            "Front of the card",
            "Back of the card\n",
        )
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
    got = ankify.Deck.from_doc(doc)
    want = ankify.Deck("").withCard(
        ankify.Card(
            "How to quit Vim",
            """
```
:q
:quit!
:wq
<S-z><S-z>
```
""",
        )
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
    got = ankify.Deck.from_doc(doc)
    want = ankify.Deck("").withCard(
        ankify.Card(
            "A tiddly-bit of Javascript",
            """
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
        )
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
    got = ankify.Deck.from_doc(doc)
    want = ankify.Deck("").withCard(
        ankify.Card(
            "Here's just some text",
            """
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
        )
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

    got = ankify.Deck.from_doc(doc)
    want = ankify.Deck("").withCard(
        ankify.Card(
            "Cool command-line tools",
            """
| Tool | What's cool |
|------|-------------|
| sed | replace things in streams of text |
| find | find files |
| awk | process files |

""",
        )
    )

    assert got == want


def test_card_back_renders_as_html():
    got = ankify.Card(
        "front",
        """
| Tool | What's cool |
|------|-------------|
| sed | replace things in streams of text |
| find | find files |
| awk | process files |

""",
    ).render_back()

    want = (
        "<table>\n"
        "<thead>\n"
        "<tr>\n"
        "  <th>Tool</th>\n"
        "  <th>What's cool</th>\n"
        "</tr>\n"
        "</thead>\n"
        "<tbody>\n"
        "<tr>\n"
        "  <td>sed</td>\n"
        "  <td>replace things in streams of text</td>\n"
        "</tr>\n"
        "<tr>\n"
        "  <td>find</td>\n"
        "  <td>find files</td>\n"
        "</tr>\n"
        "<tr>\n"
        "  <td>awk</td>\n"
        "  <td>process files</td>\n"
        "</tr>\n"
        "</tbody>\n"
        "</table>\n"
    )

    assert got == want
