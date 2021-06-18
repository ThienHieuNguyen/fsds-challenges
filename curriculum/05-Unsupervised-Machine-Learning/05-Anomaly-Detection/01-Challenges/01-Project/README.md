# 05-05

## Project - Fraud Detection

![](https://images.unsplash.com/photo-1536821571242-75b70c679796?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1072&q=80)
Photo by [rawpixel](https://unsplash.com/photos/HJENWbX4t-Q)

## Objectives

The goal is to identify fraudulent credit card transactions 💳.

## Guidelines

Fraud detection is a billion dollars business 💰: according to the [Nilson Report](https://nilsonreport.com/), credit card fraud adds up to 24 billion dollars in 2018 ! 

Every bank and insurance company has some fraud detection algorithms. They are working hard to find out the fraudulent transactions amongst a huge number of valid ones.

Some companies are doing really good. For instance, Paypal has developed really complicated and efficient algorithms to perform fraud detection.

👉🏻 Today, we will use our new skills in anomaly detection in order to build our fist fraud detection solution.

⚠️ Once again, do not rush into the model building. Take your time to understand the data and make a proper EDA. Then try to compare both the supervised and unsupervised models performance.

## Dataset

📥 You can download the dataset on [Kaggle](https://www.kaggle.com/mlg-ulb/creditcardfraud). To avoid any Github issue, don't forget to store the dataset in your local `data` folder.

Here are the features:
 1. Time: time in seconds relative to the first transaction
 2. V1 to V28: PCA outputs
 3. Amount: the amount of the transaction
 4. Class: whether the transaction is fraudulent (1) or not (0)

⚠️ This dataset is a bit different from all you've seen up to now :
- The features are mostly **outputs from a PCA**. Indeed, some data are highly protected (e.g. bank accounts information) and as a data scientist you may face this kind of data in your future jobs. Having no information on the features does not mean they cannot be understood. A proper EDA will help you to get some insights on the data.
- The dataset is **highly imbalanced** since most of the data are labelled with class 0. As you will see, less than 1% of the data is fraudulent. This means some precautions must be taken in order to evaluate your model.