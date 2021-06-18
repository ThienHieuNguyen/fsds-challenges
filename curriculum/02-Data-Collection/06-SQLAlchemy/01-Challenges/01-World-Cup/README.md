## Challenge - Ramenez la coupe à la maison ⚽️

![](https://m.media-amazon.com/images/M/MV5BNTBiZDM3NzAtNzNlMS00YmVkLWJmM2MtNWMwOTQyOWJlMzBiXkEyXkFqcGdeQXVyNDg4MjkzNDk@._V1_.jpg)

## Objectives

Use the database `sport.db` from **2018 Football World Cup** 🏆 directly in Python.

## Guidelines

- Let's work again on the exercise **World Cup** from the SQL lesson. The point here is to try to solve the problems directly with a Python script using `sqlalchemy`

### I. Allez les bleus

- Write a SQL query that returns the `team_id` of France team 🇫🇷.

- Based on France `team_id` write a query that returns the number of matches played by France team.

- Write a SQL query that returns `person_id` and `goals_scored` (the number of scored goals) of all French players who scored a goal. Order the results by descending `goals_scored`.

  > ⚠️ **Warning**: Make sure **not** to include "Own goal" of a team player not playing for France

- Write a SQL query that returns the same result as before but with the player `name` instead of the `person_id`. Which French player scored the most? Is the data clean?

- Write a SQL query that returns the minute at which Benjamin Pavard scored his "Demi-volée" goal.

### II. Best strikers

- Write a SQL query that returns the `name`, the `team name` and the number of `goals_scored` of the 3 players who scored the most goals (excluding own goals)in the competition.

### III. Stats per country

- Write a SQL query that returns all teams that played with the fields `nb_games_played`, `nb_games_win`, `nb_games_lost`, `nb_games_draw`. Order the results by `nb_games_played` descending, `nb_games_win` descending, `nb_games_draw` descending, and `team_name` ascending.

  > 🔦 **Hint**: Go **step-by-step** when constructing your SQL query. At the look of the `games` table, construct first a table that answers the question for team playing "at home" - then for team playing "outside" - then combine both.

- Write a query that returns those results for Asian team(s) that played more than 3 games.

- Write a query that returns those results for African team(s) that lost all their game.

### IV. Bonus
- Build your own ORM : create classes with relevant attributes and methods, using the previous queries. Try to answer the previous questions using your classes and instances.

Your program must be written in `src/world_cup.py`.