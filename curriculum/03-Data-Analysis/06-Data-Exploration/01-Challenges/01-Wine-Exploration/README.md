# 03-04

## Challenge 01 - Wine-Exploration 🍷

---

![](https://images.unsplash.com/photo-1423483641154-5411ec9c0ddf?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=80)

Photo by [Maja Petric](https://unsplash.com/@majapetric)

## Instructions

Now it is time for you to build your own data analysis!

Today, you will download an open source dataset, run a deep Exploratory Data Analysis (EDA), and present your results to the classroom.

The dataset to be analyzed is the following one: [Wine Reviews data](https://www.kaggle.com/zynicide/wine-reviews/data)

> Wine Reviews Dataset contains **130k wine reviews** with variety, location, winery, price, and description 🍷
>
> If you wonder how this data was collected, it was **scraped** from [Wine Enthusiast](https://www.winemag.com/?s=&drink_type=wine).

The goal of this challenge is to **explore the data**, to **run a structured analysis**, and to **present your results in a clear and concise** way.

Be structured, yet creative!

Read entirely the instructions below before starting the challenge.

## Guidelines

You are free to perform the analysis the way you want. However we recommend you to explore and run your analysis through Jupyter notebook and to present your conclusions in a structured Jupyter notebook with text and titles for organizing your results.

Please find below the usual EDA steps. The order is important but not necessarily set in stone, feel free to explore/got off the beaten track and to experiment!

### 1. Exploration

1. Load the dataset (most likely into a Pandas DataFrame)
2. Describe briefly the data. How big is your dataset? What does it contain (columns and rows)?
What type of variables does it contain (continuous, discrete)? etc.
3. Extract some first summary statistics and start understanding the distribution of your data (`data.describe()`, `data.info()`, `sns.pairplot(data)`, etc.)

### 2. Cleaning

Check if anything suspicious (missing data, N/A values, duplicated lines,
data not properly loaded, etc.) and act on it.

### 3. Analysis

1. Structure your analysis by writing a few questions you wish to answer or hypothesis
you wish to confirm/infirm
2. Aggregate the data you wish to visualize
3. Visualize those data
4. Conclude on your question/hypothesis - or finetune it - and repeat.

### 4. Presentation

At the end of the day, you will present the results of your work to the crowd with a 5-10 min pitch session followed by a small Q&A.

Feel free to choose the format you are most comfortable with for the presentation.

-- 

## Hints

If you are stuck or not sure what to explore, try answering these questions. These are just examples 🙂 :

- How are distributed the variables points? ratings? How does this distribution change depending on countries/provinces/winery?
- Which provinces produce the more wine?
- Which provinces/countries have higher rating? lower rating? Does quantity mean quality?
- Which provinces/winery produce the most expensive wines?
- Is there a reciprocal relationship between price and ratings?
- Is the some kind of relationship between description length and ratings?
- etc.
