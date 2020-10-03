# Some Notes

Stuff text.
Yes.

## notes

1. _Meet the Dot command_

    * Repeat the last change with `.` the most powerful and versatile command in Vim 💪
    * See the [docs](https://vimhelp.org/repeat.txt.html#.)

1. _Don't repeat yourself_

   * Reduce extraneous movement, because you loose the benefit of the `.` command
   * Get two for the price of one by using compound commands instead of their long-hand form:

     | `compound` | `long-hand` | effect | docs |
     |------------|-------------|--------|------|
     | `C` | `c$` | replace until the end of the line | [docs](https://vimhelp.org/change.txt.html#C) |
     | `s` | `cl` | replace single character | [docs](https://vimhelp.org/change.txt.html#s) |
     | `S` | `^C` | replace entire line | [docs](https://vimhelp.org/change.txt.html#S) |
     | `I` | `^i` | insert at beginning of the line | [docs](https://vimhelp.org/change.txt.html#I) |
     | `A` | `$a` | insert at the end of the line | [docs](https://vimhelp.org/change.txt.html#A) |
     | `o` | `A<CR>` | insert a line below | [docs](https://vimhelp.org/insert.txt.html#o) |
     | `O` | `ko` |insert a line above | [docs](https://vimhelp.org/insert.txt.html#O) |

     All these commands switch from Normal to Insert mode

1. _Take one step back, then three forward_

   * Make the change repeatable with `.` and undo with `u`
   * Make the motion repeatable with `;` and reversable with `,`

