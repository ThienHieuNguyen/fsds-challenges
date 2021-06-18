# 01-03

## Challenge 03 - Guessing Game

![](https://images.unsplash.com/photo-1502570149819-b2260483d302?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80)
Photo by [Nick Hillier](https://unsplash.com/photos/yD5rv8_WzxA)

## Objectives
Implement a simple guessing game

## Guidelines
Generate a random number between 1 and 99 (included). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

Keep the game going until the user types “exit”. Keep track of the number of trials: when the game ends, print it out.

Your program must be written in `src/guessing_game.py`. You may need to use the `randint` method from the `random` module.

The output of your program should look like this:
```
What's your guess between 1 and 99? 50
Too high!
What's your guess between 1 and 99? 25
Too low!
What's your guess between 1 and 99? 30
Congratulations, you've got it!
And it only took you only 3 trials!
```