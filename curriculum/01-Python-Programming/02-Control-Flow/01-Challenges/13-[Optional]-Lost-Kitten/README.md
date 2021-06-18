# Challenge - Help kitten get home

[](https://images.unsplash.com/photo-1560114928-40f1f1eb26a0?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80)

A kitten is lost is a plan of dimensions 40x20. His home is somewhere on the plan, let's help him get home !

At the beginning of your programme, you get the following informations :
- `init_x` : the initial position of your kitten on the x axis;
- `init_y` : the initial position of your kitten on the y axis;
- `home_x` : the position of the kitten's house on the x axis;
- `home_y` : the position of the kitten's house on the y axis.

This kitten can move in 8 directions : `N`, `NW`, `E`, `SE`, `S`, `SW`, `W`, `NW`.

At each step of your programme, write the direction in which the kitten should move to get home, and make him move one step in this correct direction.

**BEWARE** : your kitten must stay on the plan ! If at any point, your kitten's position on the x axis is above 40, or its position on the y axis above 20, your programme should raise an error.

**Bonus** : Explore the library `matplotlib.pyplot` (find the documentation [here](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.html)) and plot the deplacements of your kitten between his start point and his home.
