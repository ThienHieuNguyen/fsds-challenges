# Challenge - I Robot

![](https://images.unsplash.com/photo-1472457897821-70d3819a0e24?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1349&q=80)
Photo by [Daniel Cheung](https://unsplash.com/photos/cPF2nlWcMY4)

## Objectives
Control the movements of a basic robot

## Guidelines
The robot starts from the original point (0,0). It can move toward UP, DOWN, LEFT and RIGHT with given steps.

Write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.

The program should work like this:
```
Initial position: (0, 0)
What's your next move?
>> up 5
New position : (0, 5)
What's your next move?
>> right 4
New position : (4, 5)
What's your next move?
>> down 11
New position : (4, -6)
What's your next move?
>> left 1
New position : (3, -6)
What's your next move?
>> quit
Distance from origin: 7
```

Your program must be written in `src/i_robot.py`. You may need to use a method from the `math` module.
