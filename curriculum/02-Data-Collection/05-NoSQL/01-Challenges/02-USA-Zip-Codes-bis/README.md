## Challenge - USA Zip Codes Bis 🇺🇸

![](https://images.unsplash.com/photo-1500277127996-2e6206b069ef?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80 )

---

## Instructions

We'll do the exact same challenge as the first one, but instead of using the **Mongodb Shell** we'll be using here **Pymongo**.

### I. Create

- Open your terminal and connect to zips collection using **Pymongo**.

- Display all databases and make sure `vivadata` is there.

- Use the `vivadata` database and select the `zips` collection.

- Follow the same structure of existing documents and add three new documents for three different districts in Paris (like the 13th, 14th and 15th district). The `_id` must be the district zip code and the state must be `Île-de-France`.

### II. Read

- Display all zip codes for the city of New York (display only the zip code).

- Count the total number of New York city zip codes.

- Count the number of all zip code areas in the city of New York, Los Angeles and  Nashville.

- Display the list of cities with no duplicates.

- Select the ten most populated zip code areas where population is bellow than 20 000, sorted by population.

- Select zip codes areas with a population greater than 40 000 and part of a city starting with "NA".

- Use aggregation and display the 10 most populated cities.

- Use aggregation and give the list of the three most populated cities in the state of Texas ("TX")

### III. Update

- For the Paris zip codes you've created, update `state` to have the value `France`.

- For one of the Paris zip codes you've created, add a new field called `monuments` and try to put in this field a list of 3 famous monuments from this district.

- Change the  second monument and put your name instead.

- Delete the field `monuments` from all your documents.

### III. Delete

- Delete all zip codes that are in France.



