# 01-03

## Challenge 09 - Towers of Hanoi

![](https://images.unsplash.com/photo-1528649659491-23edddd0b98a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1351&q=80)
Photo by [Andre Ouellet](https://unsplash.com/photos/cga32YQt0Kw)

## Objectives
Implement a "Towers of Hanoi" game

## Guidelines
The game uses three poles. A number of disks is stacked in decreasing order from the bottom to the top of one pole, i.e. the largest disk at the bottom and the smallest one on top. The disks build a conical tower. 

The aim of the game is to move the tower of disks from one pole to another pole. The number of moves necessary to move a tower with n disks can be calculated as 2<sup>n</sup> - 1.

The following rules have to be respected:
- only one disk may be moved at a time
- only the most upper disk from one of the poles can be moved in a move
- it can be put on another pole, if this pole is empty or if the most upper disk of this pole is larger than the one which is moved.

Your program must be written in `src/tower_of_hanoi.py`.