# 04-06

## Challenge 02 - Airbnb Optimization

---

![](https://www.kent.ac.uk/events/images/paris-notre-dame-1920x1280.jpg)

## Instructions

Today, we will continue improving our **Airbnb price prediction model**.

Especially, we will focus on carefully selecting the features that appear interesting in running the predictions, and we will prepare them in order to train our Machine Learning model.

Additionally, once we are happy with our selected features, we will seek to optimize the hyperparameters of our model. As the dataset is quite big, you will need to select a *sample* of your data to search for the optimal hyperparameters.

As a reminder, we detail again the steps you can follow to proceed in building your Machine Learning model (with the new step *4. Hyperparameters Optimization*).

## Guidelines

You are free to perform the analysis the way you want. However we recommend you to explore and run your analysis through Jupyter notebook and to present your conclusions in a structured Jupyter notebook with text and titles for organizing your results.

Please find below some structure you can follow to proceed in this challenge. Feel free to explore on your own and to go off the beaten tracks.

### 1. EDA

1. Load the dataset (most likely into a Pandas DataFrame). You should already have downloaded the dataset during *Data Visualization* challenge.
2. Describe briefly the data, explore important variables and possible relationships between variables.
3. Clean your data (missing data, N/A values, duplicated lines, outliers, data not properly loaded, etc.) and act on it.
4. Ask questions about your data and try answering them. Visualize your data and understand it.

### 2. Features Preparation

1. Think about the features you want to select for your models, prepare them if needed (categorical...)
2. Create new smart features
3. Scale your features

### 3. Model Training

1. Split your dataset into training set and test set. You can also split into training, validation and testing set if appropriate (for optimizing hyperparameters for example or comparing performance of your models).
2. Choose a model that you think appropriate and train it on your data.

### 4. Hyperparameters Optimization

1. Choose the hyperparameters you wish to optimize
2. Sample your data in order to find the optimal hyperparameters on a subset of your data
2. Run a search strategy (`GridSearchCV` or `RandomSearchCV`) to find the optimal hyperparameters on your sample dataset, and retrain on your complete dataset

### 5. Conclusions

1. Evaluate your model, think about what metrics make more sense.
2. Iterate on your analysis: go back to your EDA and features and think whether you can improve your data preparation
3. Present your results in a clear and visual way.
