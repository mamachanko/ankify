# Ankify 📝 → 🗃

> Create [Anki](https://apps.ankiweb.net) decks from Markdown notes 

Let's say you've reading a book about command line tools and took these notes:
```
# Command line tools

1. _How to exit Vim_
 `:wq`, `:x` or `ZZ`

1. _Cool tools_
 * xargs
 * awk
```

Ankify will write a deck to `notes.apkg` called _My Notes_ with two cards:
| Front | Back |
|-------|------|
| How to exit Vim|`:wq`, `:x` or `ZZ`|
| Cool tools | <ul><li>xargs</li><li>awk</li></ul> |

Now you can import `notes.apkg` into Anki.

## Installation & usage

> ⚠️  this is work-in-progress. none of these work ... yet. stay tuned. 🦺

### As a Python module
```
$ pip install ankify
$ python
>>> import ankify
>>> ankify.ankify('notes.md', 'notes.apkg')
```

### On the command-line
```
$ pip install ankify
$ cat notes | python -m ankify > notes.apk
```

### Using docker

```
$ cat notes | docker run -i mamachanko/ankify > notes.apkg
```

### Using the API
```
$ curl --method POST --data @notes.md --output notes.apkg --url https://ankify.io
```

## todos
 * [x] fix markdown rendering
 * [x] validate that reading from stdin amd writing to stdout works with docker run
 * [x] investigate what the workflow of updating cards and re-importing a deck
   would look like
 * [] return stabel guids for notes (see [here](https://github.com/kerrickstaley/genanki#note-guids))
 * [] set card number
 * [] read from stdin
 * [] write to stdout
 * [x] refactor to classes
 * [] build docker image
 * [] publish image
 * [] create ankify website
 * [] break out ankify.py, docker and web repositories 
 * [] get domain
 * [] publish module to pypi
 * [] make module invokeable through 'python -m ankify'
 * [] create ankify org

