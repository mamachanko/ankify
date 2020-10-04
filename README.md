# Ankify 📝 → 🗃

> Create [Anki](https://apps.ankiweb.net) decks from Markdown notes 

```
cat << EOF | ankify > notes.apkg
# My Notes
1. _How to exit Vim_
 `:wq`, `:x` or `ZZ`
1. _Cool tools_
 * xargs
 * awk
EOF
```
Will write a deck to `notes.apkg` called _My Notes_ with two cards:
| Front | Back |
|-------|------|
| How to exit Vim|`:wq`, `:x` or `ZZ`|
| Cool tools | <ul><li>xargs</li><li>awk</li></ul> |
    
Now you can import `notes.apkg` into Anki.

## todos
 * [x] fix markdown rendering
 * [x] validate that reading from stdin amd writing to stdout works with docker run
 * [] read from stdin
 * [] write to stdout
 * [] refactor to classes
 * [] build docker image
 * [] publish image
 * [] create ankify website
 * [] break out ankify.py, docker and web repositories 
 * [] get domain
 * [] publish module to pypi
 * [] make module invokeable through 'python -m ankify'
 * [] create ankify org

