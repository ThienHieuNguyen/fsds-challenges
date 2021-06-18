# 01-03

## Challenge 08 - Magic Number

![](https://images.unsplash.com/photo-1513002433973-e0a181372d60?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80)
Picture by [Wayne Low](https://unsplash.com/photos/OvN4OkhkTLo)

## Objectives
This exercise is a little bit more difficult. You will need to combine everything you've learned so far.

## Guidelines
The goal is to find the smallest number (let's call it N) such that:
- if N obeys property X, then the digit X is part of the number;
- if N does not obey property X, then the digit X is NOT part of the number.

For example, if 5419 was a magic number, it would obey properties 1, 4, 5, 9 and not 0, 2, 3, 6, 7, 8.

Your program must be written in `src/magic-number.py`

### Properties
0. One of the digits of M is the sum of the others.
1. Digits in decreasing sequence.
2. M has at least 2 odd digits.
3. All digits are different.
4. There is no subset in the digits with a sum of 4.
5. The number is not a palindrome.
6. The number does not contain 3 odd digits in a row.
7. M is a prime number.
8. M has at least 2 even digits in a row.
9. The product of all odd digits is a square number.

### Bonus
Can you find the smallest magic number, depending on the way the properties are ordered ?