# 02-04

## Challenge 02 - "Ramenez la coupe à la maison" 🏆

---

![](https://m.media-amazon.com/images/M/MV5BNTBiZDM3NzAtNzNlMS00YmVkLWJmM2MtNWMwOTQyOWJlMzBiXkEyXkFqcGdeQXVyNDg4MjkzNDk@._V1_.jpg)

## Instructions

You are given a database `sport.db` that contains data from **2018 Soccer World Cup**.

### I. Data introduction

- What **tables** does it contain?

- What is the structure of the table `games`? How many games were played in total?

- What is the structure of the table `teams`? How many teams participated in the competition?

### II. Allez les bleus

- Write a SQL query that returns the `team_id` of France team 🇫🇷.

- Based on France `team_id` write a query that returns the number of matches played by France team.

- Write a SQL query that returns `person_id` and `goals_scored` (the number of scored goals) of all French players who scored a goal. Order the results by descending `goals_scored`.

  > ⚠️ **Warning**: Make sure **not** to include "Own goal" of a team player not playing for France

- Write a SQL query that returns the same result as before but with the player `name` instead of the `person_id`. Which French player scored the most? Is the data clean?

- Write a SQL query that returns the minute at which Benjamin Pavard scored his "Demi-volée" goal.

### III. Best strikers

- Write a SQL query that returns the `name`, the `team name` and the number of `goals_scored` of the 3 players who scored the most goals (excluding own goals)in the competition.

### IV. Stats per country

- Write a SQL query that returns all teams that played with the fields `nb_games_played`, `nb_games_win`, `nb_games_lost`, `nb_games_draw`. Order the results by `nb_games_played` descending, `nb_games_win` descending, `nb_games_draw` descending, and `team_name` ascending.

  > 🔦 **Hint**: Go **step-by-step** when constructing your SQL query. At the look of the `games` table, construct first a table that answers the question for team playing "at home" - then for team playing "outside" - then combine both.

- Write a query that returns those results for Asian team(s) that played more than 3 games.

- Write a query that returns those results for African team(s) that lost all their game.

- [BONUS] Write a query that returns those results for all countries plus the fields `nb_goals_scored`, `nb_scores_collected`.
