All solutions are written and created by John Robson Wed Mar 31, 2021

These are the basic (MVP: minimal viable product) answers. Please see the advanced solutions for other answers.

NOTES: You cannot use "div", ".table", or "div.table" to access the main container div.
It will fail even if the code is right.

Level 1:
    plate

Level 2:
    bento

Level 3:
    #fancy

Level 4:
    plate apple

Level 5:
    #fancy pickle

Level 6:
    .small

Level 7:
    orange.small

Level 8:
    bento orange.small

Level 9:
    :is(plate, bento)   //newer solution (my preferred way)
    plate, bento        //traditional solution

Level 10:
    *

Level 11:
    plate *

Level 12:
    plate + apple

Level 13:
    bento ~ pickle
    pickle ~ pickle     //either answer is perfectly fine

Level 14:
    plate > apple

Level 15:
    plate orange:first-child

Level 16:
    plate :only-child
    plate > :only-child   //either answer is perfectly fine

Level 17:
    .small:last-child

Level 18:
    plate:nth-child(3)

Level 19:
    bento:nth-last-child(3)

Level 20:
    apple:first-of-type

Level 21:
    :nth-of-type(even)

Level 22:
    :nth-of-type(2n+3)

Level 23:
    apple:only-of-type

Level 24:
    .small:last-of-type

Level 25:
    bento:empty

Level 26:
    apple:not(.small)

Level 27:
    [for]

Level 28:
    plate[for]

Level 29:
    bento[for="Vitaly"]

Level 30:
    [for^="Sa"]

Level 31:
    [for$="ato"]

Level 32:
    [for*="obb"]