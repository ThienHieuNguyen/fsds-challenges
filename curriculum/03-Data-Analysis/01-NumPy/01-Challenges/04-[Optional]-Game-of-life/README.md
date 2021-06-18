# 03-01

## Challenge 03 - Game of Life
![](https://i.ytimg.com/vi/QT_pKNzOOhQ/maxresdefault.jpg)

## Objectives
Implement your own version of [Conway’s Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life). 

You can start by watching [this nice video](https://www.youtube.com/watch?v=S-W0NX97DB0) about the game.

## Guidelines
Conways’s Game of Life is a Cellular Automation Method created by John Conway. The game is a zero-player game: its evolution is only determined by the initial state, called the seed of the system.

The value of any cell at a given instant depends on the state of its neighbors at the previous time step. There are 4 rules:
- a live cell with fewer than two live neighbors dies, as if by underpopulation.
- a live cell with two or three live neighbors lives on to the next generation.
- a live cell with more than three live neighbors dies, as if by overpopulation.
- a dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

### How to make it work ?
1. Create a NxN `grid` of random zeros and ones to initialize the game.
2. Pad the grid with zeros in order to perform easier calculations.
3. Write a function to update each given cell(i, j) in the grid with its number of alive neighbours.
4. Update the value of each cell in the grid with their number of alive neighbours.
5. Apply Conway's rules and update the grid display.
6. Imagine a fancy display of your grid in the console !