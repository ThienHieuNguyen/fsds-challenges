# 01-04

## Challenge 01 - Bank Account

![](https://images.unsplash.com/photo-1534322869500-14fc9f5f5767?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1650&q=80)
Picture by [rawpixel](https://unsplash.com/photos/LTxCtKYw-_E)

## Objectives
Model a bank account to improve your OOP skills.

## Guidelines
1. Write a class `Account` :
- the account has some data, typically the `name` of the account holder, the `account_number`, and the current `balance` (2000 by default).
- Three things we can do with an account is `withdraw` money, `deposit` money into the account, and `dump` (print out) the data of the account.

Instanciate two accounts for Ross and Rachel with random account numbers. Deposit and withdraw some money a couple of times. Then dump the informations on both accounts. The output should look like this:
```
ross_account.dump()
Ross, 9502018482, 1350
rachel_account.dump()
Rachel, 1945729572, 3450
```

2. Try now to instanciate directly bank accounts from your iPython console and play with them. Hint: you may have to use an `import` while being in the appropriate folder.

Your program must be written in `src/bank_account.py`.