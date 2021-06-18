## Challenge - USA Zip Codes 🇺🇸

![](https://images.unsplash.com/photo-1500277127996-2e6206b069ef?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80 )

---

## Instructions

We'll be using for this challenge the dataset seen during the course, `zips.json`. The main objective here is to give you a chance to practice `CRUD` (`Create`, `Read`, `Update` & `Delete`) operations. The dataset you'll have to manipulate has the following elements as fields :
- **_id** : The zip code, in this case we didn't use the type `ObjectId` but the zip code itself because it assures unicity.
- **city** : The name of the city containing the zip code. We can have many zip codes linked to one city.
- **pop** : The number of people living in the zip code area.
- **loc** : Location of the zip code area by longitude and latitude.
- **state** : City's State code.

### I. Create
- Open your terminal and launch the MongoDB server.

- Open a new terminal and load the dataset contained inside `zips.json` into a database that you will name `vivadata` and your collection has to be named `zips`.


- Open the MongoDB shell.


- Display all databases and make sure the newly created one `vivadata` is there.


- Use the `vivadata` database.


- Display all present collections.


- Follow the same structure of existing documents and add three new documents for three different districts in Paris (like the 13th, 14th and 15th district). The `_id` must be the district zip code and the state must be `Île-de-France`.

### II. Read

- Select all zip codes for the city of New York (display only the zip code).

- Count the total number of New York city zip codes.

- Count the number of all zip code areas in the city of New York, Los Angeles and Nashville.

- Display the list of cities with no duplicates.

- Select the ten most populated zip code areas where population is below 20 000, sorted by population.

- Select zip codes areas with a population greater than 40 000 and part of a city whose name starts with "NA".

- Use aggregation and display the 10 most populated cities.

- Use aggregation and give the list of the three most populated cities in the state of Texas ("TX").


### III. Update

- For the Paris zip codes you've created, update `state` to have the value `France`.


- For one of the Paris zip codes you've created, add a new field called `monuments` and try to put in this field a list of 3 famous monuments from this district.


- Change the  second monument and put your name instead.


- Delete the field `monuments` from all your documents.


### III. Delete

- Delete all zip codes that are in France.


