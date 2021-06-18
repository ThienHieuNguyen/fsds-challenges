# 02-01

## Challenge 03 - Hangman Game

![](https://www.regles-jeux-plein-air.com/wp-content/uploads/2015/04/Le-Pendu.png?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjEyMDd9)



## Objectives
Implement a Hangman game

## Guidelines

In this exercise, we will implement a [Hangman game](https://en.wikipedia.org/wiki/Hangman_(game)) .The goal is to guess a secret word letter by letter.

#### 1. Pick a random secret word
  
You have access to a file `nordig-sowpods.txt` listing all words in english language allowed for scrabble. We'll use this list for our game.

Import a random word from the file: it will be the `secret_word` to guess.

#### 2. Write the guessing routine

It should work like this:
```
Let's start a Hangman Game !
I've picked a word, can you guess it ?

Word = _ _ _ _ _ _ _
Remaining attempts : 6/8
Misses :

>> Pick a letter: A
Good job !

Word = _ A _ _ _ A _
Remaining attempts : 6/8
Misses :

>> Pick a letter: E
Try again !

Word = _ A _ _ _ A _
Remaining attempts : 5/8
Misses : E

...

Word = H A N G _ A N
Remaining attempts : 4/8
Misses : E, U, F, L

>> Pick a letter: M
Congratulations, you've guessed the secret word HANGMAN in 10 rounds !

Do you want to play again (y/n) ?
```
#### 3. Store the scores and print the Top5 while leaving the game

You should ask for the player's name before launching the game.

The players a ranked by :
1. number of missed letters
2. numbers of attempts
3. game time


```
BEST SCORES
-----------------------------------------------------------------------
Player   | Numbers of missed letters | Number of attempts | Game time
-----------------------------------------------------------------------
Phoebe   |            0              |          5         |    1:12
Chandle  |            0              |          3         |    0:36
Rachel   |            1              |          4         |    0:56
Joey     |            2              |          8         |    1:05
Monica   |            2              |          8         |    1:17
```
The scores should be stored in `input/scores`. Of course, if you score in the top5, the ranking has to be modified.


## Bonus

Try to display the Hangman in your console while playing the game
```
________
|/     |
|      O
|     /X\
|     / \
|
|________
```