## Challenge - Amazon Books 📚

![](https://images.unsplash.com/photo-1512820790803-83ca734da794?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1150&q=40)

---

## Instructions

We'll be working now with a dataset containing some Amazon books. You can find this dataset here in this same folder in `books.json`. Basically, what we have here as information is the book title, a long and a short description, authors, categories, pages count and the book status. Again this time, we'll be using **Pymongo**.

### I. Data Discovery

- Load the dataset in the `vivadata` database, in a collection named `books`.

- Connect to the collection.

- Try to display some documents to get a grasp of the documents structure.

- Display all possible book status value possible.

- The number of books for each status.

- Display all existing book categories, a list with no duplicates.

- Plot a graph showing the frequency distribution of the page counts with 20 bins. (hint : use https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.hist.html)

### II. Data Cleaning

- As we've seen there is a problem with the existing categories, either we have many categories meaning the same thing (as `Microsoft/.NET`, `Microsoft .NET` and `.NET`), categories with a little type or categories that doesn't make any sense. Try to clean this by deleting the categories that doesn't mean anything and unify the different categories with different syntaxes under the same name.

- The histogram you've plotted before shows a huge spike near zero. It makes no sense to have books with zero pages. Clean this by replacing a page count equal to zero to a null value. Redo the plot of the histogram.


### III. Scraping thumbnails

- Add a new field to all documents named `scrapped` with a default value equal to `0`.

- In your collection there is a field containing the web address to the book's thumbnail. Write a script that will save those thumbnails into a local folder named `thumbnails` and each time you've scraped one update the  `scrapped` value to `1`. Consider the `isbn` code as a name and also the fact that you may encounter some issues when the `isbn` or the thumbnail doesn't exist or has no value.

  
