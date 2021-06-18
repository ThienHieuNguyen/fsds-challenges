# 01-04

## Challenge 03 - Vehicles

![](https://images.unsplash.com/photo-1521706887145-1c0edacadb25?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1268&q=80)
Picture by [chuttersnap](https://unsplash.com/photos/d271d_SOGR8)

## Objectives
Inheritance and properties

## Guidelines
1. Write a class `Vehicle` :
- a vehicle is defined by the attributes `year`, `brand`, `color`, `wheels`, `consumption`, `fuel`, `kilometers`. It also has `speed` which is always zero when the vehicle is instanciated.
- write methods to `start`, `stop`, `accelerate` and `brake` with an increment or decrement of speed by 10 each time it is called.

2. Start a timer when the vehicle `start` and stop the timer when the vehicle `stop`. Meanwhile, update the `kilometers`and the `fuel` depending on the driving (`speed`, `accelerate` and `stop`)

3. Write two new classes `Car` and `Motorbikes`. Imagine what could change in the attributes and methods.

4. Review the control access in all the previous classes.

Your program must be written in `src/vehicle.py`. You should be able to instanciate circles and play with them directly from your iPython console.