# 02-04

## Challenge 04 - Coding Bootcamp 💻

---

![](https://i2.wp.com/blockpublisher.com/wp-content/uploads/2018/11/mikito-tateisi-333584-unsplash.jpg?resize=780%2C405&ssl=1)

---

## Instructions

You just joined an amazing coding bootcamp that lasts 3 months. The start date of the bootcamp is January 01, 2019 and the end date is March 31, 2019.

Each day, students from the bootcamp can make submissions.

Write a query that returns per day, **the number of unique students that made at least one submission each day** (for each day of the bootcamp, sorted by day and starting on the first day of the bootcamp).

This query should also return id and name of the student who made the maximum number of submissions each day. In case of equality, print the lowest `student_id`.


## Example

The input looks like this:

  ``` sql
  CREATE TABLE Students (
      student_id integer NOT NULL,
      student_name VARCHAR(50) NOT NULL,
      UNIQUE(student_id)
  );
  ```
  ``` sql
  CREATE TABLE Submissions (
      submission_id INTEGER NOT NULL,
      submission_date DATE NOT NULL,
      student_id INTEGER NOT NULL,
      score INTEGER NOT NULL,
      UNIQUE(submission_id)
  );
  ```

- **Students**:
```
 student_id | student_name
------------+--------
       1038 | Sophie
       1431 | Antoine
       2483 | Alexandra
       4903 | Vincent
       6508 | Anna
       9032 | Nicolas
       ...
```

- **Submissions**:
```
submission_date |    submission_id    | student_id | score
----------------+---------------------+------------+--------
   2019-01-01   |   303940132301      |    1038    | 100
   2019-01-01   |   130480318403      |    1431    | 0
   2019-01-01   |   831043031943      |    9032    | 10
   2019-01-01   |   590342959301      |    6508    | 50
   2019-01-01   |   131853015833      |    4903    | 0
   2019-01-01   |   586031581309      |    2483    | 100
   2019-01-02   |   684012549310      |    4903    | 10
   2019-01-02   |   103853153849      |    6508    | 100
   2019-01-02   |   864205892043      |    1038    | 20
   2019-01-02   |   391850314904      |    4903    | 100
   2019-01-03   |   406429059423      |    1038    | 0
   2019-01-03   |   593014043158      |    2483    | 30
   2019-01-03   |   684205931431      |    9032    | 80
   2019-01-03   |   314803143801      |    1038    | 50
   2019-01-04   |   642805932043      |    2483    | 10
   2019-01-04   |   542981493014      |    6508    | 0
   2019-01-05   |   358420592043      |    2483    | 100
   ...
```

Your query should **return**:

```
2019-01-01  |  6  |  1038  |  Sophie
2019-01-02  |  3  |  4903  |  Vincent
2019-01-03  |  2  |  1038  |  Sophie
2019-01-04  |  1  |  2483  |  Alexandra
2019-01-05  |  1  |  2483  |  Alexandra
```
