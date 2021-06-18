# Challenge - Change

![](https://images.unsplash.com/photo-1534951009808-766178b47a4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80)

## Guidelines

Let's help a cashier in a supermarket to manage their cash register in the most efficient way.
Our cashier only has bills of 10€, 5€ and coins of 2€ in their cash registry.

Write a function `change()` returning a dictionary representing the most efficient way to return change on a given amount of cash (e.g. the one using the smallest number of bills/coins).

If it is impossible to give change on an amount, your function should return a message indicating that the transaction is impossible.

**Example :**

- For an amount of cash of `147€`, your function should return `{'ten': 14, 'five': 1, ''two': 1}`
- For an amount of cash of `1€`, your function should return `"Transaction impossible"`
