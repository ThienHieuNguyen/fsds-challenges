## Challenge - Scrapping Job Offers 🕸️


![](https://images.unsplash.com/photo-1568598035424-7070b67317d2?ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=40)

---

## Instructions

This is the second part of a composed challenge to crawl job offers (from https://www.amaljob.com/liste-toutes-offres-emploi-maroc ). You will have to make sure that you've done the first part and that the **SQL** database containing the list of job offers to crawl is available. It is time to crawl some valuable informations regarding each job offer and put them into **MongoDB**.

### I. Get the list!

- By using **SQLAlchemy**, get the list of links to crawl and their IDs.

### II. Crawl and update!

- Now for each link we want to get the **region** of the job offer, **type of contract**, **mission description** and **profile description**. For each scraped link create a **MongoDB** document in a collection named `job-offers` part of a new database called `crawlers`. After crawling each link, update the status `scrapped` in the corresponding row of the **SQL** table.