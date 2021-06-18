# Challenge - Round Robin Tournament

---
![](https://images.unsplash.com/photo-1521189510502-3dbdb40d8bc0?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1349&q=80)
Photo by [rawpixel](https://unsplash.com/photos/tpLz5aKdQmM)

## Objectives
Implement an algorithm of [round robin tournament](https://en.wikipedia.org/wiki/Round-robin_tournament).

This algorithm is useful when you want a competition "in which each contestant meets all other contestants in turn", or if you have a classroom of students and want them to work in pairs, but with a different partner every day.

## Guidelines
1. Open `src/round_robin_tournament.py` with your text editor.

1. Write a `schedule` function with one argument, a list of N `students`. It will return a list `daily_teams` of N - 1 elements, where each element contains a list of tuples representing the teams of the day. Don't forget to deal with the case of an even number N.

1. Complete the `main` function to display the `daily_teams` as shown in this example :
```
Day 1: (Paul, ), (Ringo, John), (George, OtherGuy)
Day 2: (Ringo, ), (George, Paul), (OtherGuy, John)
Day 3: (George, ), (OtherGuy, Ringo), (John, Paul)
Day 4: (OtherGuy, ), (John, George), (Paul, Ringo)
Day 5: (John, ), (Paul, OtherGuy), (Ringo, George)
```
