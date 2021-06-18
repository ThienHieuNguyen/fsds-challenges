# 02-04

## Challenge 01 - Querying Spotify 🎷🎹

---

![](https://images.unsplash.com/photo-1484972759836-b93f9ef2b293?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=80)
Photo by [William Recinos](https://unsplash.com/@iwillbmm)

## Instructions

You will be using the SQL script `spotify.sql`.

This script will be used to create a (virtual) **music service database** (with tables listing tracks, artists but also customers, employees, etc.).

### I. Selection

- In your terminal, open SQlite console and run the SQL script to create the database. Which tables does it contain?

- Activate headers in SQLite

- Select all rows and all columns from the table `Album`

- Select all rows and only the column `Title` from the table `Album`

- Select the 10 first rows and only the columns `Title` and `ArtistId` from the table `Album`

- Select all the unique `ArtistId` from the table `Album`

- Select all the unique `Country` from the table `Customer`

### II. Filter

- Select all the customers with field `State` is null.

- Select all the customers `FirstName`, `LastName`, `City`, `Country`, `State`, and replace all empty values in `State` by "N/A".

- Select all the customers who have a Yahoo email address (ending by @yahoo.com, @yahoo.fr, @yahoo.be, etc.).

- Select all the Customers who have a Gmail or an Apple email address

- Select all the Customers who live in Bordeaux, Rome, or Rio de Janeiro

### III. Count

- Count the number of Albums (= number of rows in `Album` table)

- Count the number of Customers with non missing field `State`

- Count the number of unique artists that released an album. Is it the same number of artists contained in `Artist` table?

### IV. Order

- List all employees alphabetically (`LastName`, then `FirstName` in alphabetical order)

- List `FirstName` of employees with their associated `HireDate` and sort it by decreasing `HireDate`.

- List all employees `FirstName`, `Title` and `BirthDate` that are not General Manager and sort them by ascending `Title` and descending `BirthDate`

### V. Aggregate

- Retrieve the number of albums released by `ArtistId`

- Retrieve the possible different `UnitPrice` of a Track and the associated number of tracks at this price. Give this last column a correct name.

- Retrieve the list of `Composer` (non-missing) that wrote more than 20 songs and the number of songs they created (call the column `nb_songs`). Order the results by descending number of songs.
