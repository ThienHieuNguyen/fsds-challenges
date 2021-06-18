# 02-01

## Challenge 01 - Airbnb CSV

![](https://www.labtour.fr/wp-content/uploads/2016/09/airbnb_logo_detail1.png?resize=730%2C389&ssl=1?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjEyMDd9)
Picture by [j zamora](https://unsplash.com/@jzamora)

## Objectives

File katas with airbnb rentals.

## Guidelines

The `input/airbnb.csv` file contains an extract of 100 vacation rentals.

#### 1. Import the data in a list and play with it :
   - write your name as the Host Name of the ad "3-pièces proche Montorgueil Paris" 
   - change the Last Review date of the ad n°3305756 to 2019-01-07
   - increase the price of all Philippe's ad to 250
   - retrieve all the ads around Ménilmontant and store them in a file `input/menilmontant.csv` keeping only the Id, Name and Price info
   - remove the two ads close to Notre-Dame from the list
  

#### 2. Create a `Rental` class and instanciate all the ads in the `input/airbnb.csv` file.

- select only 10 ads near Panthéon with the highest numbers of reviews and store them in a `input/pantheon.bin` binary file
- open the file again and delete all the Private Rooms
- convert the remaining content of  `input/pantheon.bin` into  `input/pantheon.csv` file. 