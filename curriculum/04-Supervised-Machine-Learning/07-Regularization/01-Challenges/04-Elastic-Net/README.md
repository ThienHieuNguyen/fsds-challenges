# 04-10

## Challenge 03 - [Optional] Elastic Net

![](https://images.unsplash.com/photo-1456428746267-a1756408f782?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80)

Photo by [Clint Adair](https://unsplash.com/photos/BW0vK-FA3eg)

## Guidelines

This is an optional exercise. In this exercise, you will have to code yourself the Elastic Net algorithm. The Elastic Net is a combination of Ridge and LASSO: it adds both l1 and l2 regularizations.

The steps to recode such an algorithm would be the following:

Define first the prediction function, that takes as input features and parameters, and returns a prediction value.

Define then the loss function.

Compute the update function.

Finally put it all together in a loop over a number of iterations:
- Take random parameters
- Compute the predicted values
- Compute the loss (including regularization)
- Compute the update function
- Update parameters and repeat from step 2 

