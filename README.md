# Numerical-BrainFuck
Brainfuck work with both number and char

There are currently 13 operator, 8 extended BrainFuck operator, 5 extra.
support 69420 cells, support large int, number I/O, unicode char I/O.

Main idea of this language: Instead of interacting/changing the pointed cell, it takes next cell's value and use it to caculate.

caculation operator use next cell for caculation, Default will be used if next cell is 0.
Some of the operator are altered from normal BF and works differently:
 - `+`,`-`: Add/subtract cell`p`(pointer) by cell`p + 1` (default 1)
 - `[`,`]`,`>`,`<`: Remains same as BF.
 - `.`: output absolute of cell`p` as unicode(`chr(cell[p])`)
 - `,`: read 1 char `i` and set cell`p` to `i`'s unicode value (default 0)

Extra operator:

 - `:`: output cell`p` as an int
 - `;`: takes input until `\n` and treat it as whole int (default 0)
 - `\`: divide cell`p` value by cell`p+1` (floored)  equal to `cell[p] //=cell[p+1]` (default 2)
 - `*`: multiply cell`p` value by cell`p+1` (default 2)
 - `%`: module cell`p` value by cell`p+1` (default 1)
