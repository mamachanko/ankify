# Ankify 📝 → 🗃

> Create [Anki](https://apps.ankiweb.net) decks from Markdown notes

Let's say you've been reading a book about command line tools and took these
notes:
```
---
title: My Notes
---

# How to exit Vim

`:wq`, `:x` or `ZZ`

# Cool tools
 * xargs
 * awk
```

Ankify will create a deck called _My Notes_ with two cards:
| Front | Back |
|-------|------|
| How to exit Vim|`:wq`, `:x` or `ZZ`|
| Cool tools | <ul><li>xargs</li><li>awk</li></ul> |

You can import this deck into Anki.

## Installation & usage

### On the command-line

* Read from stdin:
  ```
  $ cat notes.md | python ankify.py > notes.apkg
  ```

* Provide a filename:
  ```
  $ python ankify.py notes.md
  ```

### Using docker

```
$ cat notes.md | docker run -i mamachanko/ankify > notes.apkg
```

## todos
 * [x] fix markdown rendering
 * [x] validate that reading from stdin amd writing to stdout works with docker run
 * [x] investigate what the workflow of updating cards and re-importing a deck
   would look like
 * [x] read from stdin
 * [x] write to stdout
 * [x] refactor to classes
 * [x] build docker image
 * [x] publish image
 * [] return stable guids for notes (see [here](https://github.com/kerrickstaley/genanki#note-guids))
 * [] set card number
 * [] automate docker image building and publishing
 * [] create ankify website
 * [] create web API
 * [] get domain
 * [] publish module to pypi
 * [] make module invokeable through 'python -m ankify'

