# 02-04

## Challenge 03 - Professions 👔

---

![](https://www.bitcoinstarterpack.net/wp-content/uploads/2018/12/hunters-race-408744-unsplash-e1544195230233.jpg)

---

## Instructions

In this exercice, you need to write two different queries:

1. Write a query that returns an alphabetically ordered list of all **names** in the table `PROFESSIONS`, immediately followed by the **first letter of each profession in parentheses**.

  For example, given this `PROFESSIONS` table:

  ```
   Name     | Occupation
  ----------+--------
  Philippe  | Doctor
  Nicolas   | Professor
  Antoine   | Professor
  Marie     | Singer
  Alexandra | Doctor
  Sophie    | Actor
  ```

  your query should return:
  ```
  Alexandra(S)
  Antoine(P)
  Marie(S)
  Nicolas(P)
  Philippe(D)
  Sophie(A)
  ```

2. Write a query that returns the **number of ocurrences** of each occupation in `PROFESSIONS`.

  Sort the occurrences in ascending order, and output them in the following format:
  `There are a total of [occupation_count] [occupation]s.`
  where [occupation_count] is the number of occurrences of an occupation in `PROFESSIONS` and [occupation] is the lowercase occupation name.

  If more than one Occupation has the same [occupation_count], they should be ordered alphabetically.

  Based on previous `PROFESSIONS` table, your query should return:
  ```
  There are a total of 1 actors.
  There are a total of 1 doctors.
  There are a total of 2 professors.
  There are a total of 2 singers.
  ```
