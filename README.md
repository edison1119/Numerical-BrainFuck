# Numerical-BrainFuck
Brainfuck work with both number and char

There are currently 13 operator, 8 extended BrainFuck operator, 5 extra.
support 69420 cells, support large int, number I/O, unicode char I/O.

Main idea of this language: Instead of interacting/changing the pointed cell, it takes next cell's value and use it to caculate.

Some of the operator are altered from normal BF and works differently:

`+`,`-`: Add/subtract value of cell`p`(pointer) with next cell(`p + 1`) value, if cell`p+1` is `0`, then default `1` is used instead.

