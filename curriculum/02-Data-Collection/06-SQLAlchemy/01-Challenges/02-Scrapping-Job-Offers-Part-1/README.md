## Challenge - Scrapping Job Offers 🕸️


![](https://images.unsplash.com/photo-1568598035424-7070b67317d2?ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=40)

---

## Instructions

This is the first part of a composed challenge to crawl job offers (from https://www.amaljob.com/liste-toutes-offres-emploi-maroc ), the second part we'll be seen in the **NoSQL** course.  Here we'll try to crawl some job offer links and list them in our **SQL** database and have them as a reference for the second part of the challenge where we will crawl the information contained on them.

### I. Database Creation

- Create a database named `JobOffersDB.db`.

- Create a table that will contain the following columns : 

  - `link_id` : a unique ID.
  - `url` : The URL to be crawled, it has to be a unique URL.
  - `title` : The title of the job offer.
  -  `scrapped` : A boolean indicator `0` if the content of the link hasn't been crawled (during the second challenge) and `1` if it was crawled. 
  - `last_scrapped`: The date and time of the last information extraction during  the second challenge.


### II. Scrapping

- Crawl, as much as possible, the links of the job offers contained here : https://www.amaljob.com/liste-toutes-offres-emploi-maroc. For each page, you just have to get the name of the job offer and the related link, that's it. Try using **SQLAlchemy** to automate your a Python writing into the newly created SQL database.