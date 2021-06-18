# Challenge - Going up the Empire State Building

![](https://images.unsplash.com/photo-1528449995200-88f6f5734325?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1053&q=80)

## Guidelines

Simulate a random walk 500x in which you start at floor 0 of the Empire State Building and in which you throw a dice 100x to determine what you will do :
- If the dice gives 1 or 2, go down 1 floor
- If the dice gives 3, 4 or 5, go up 1 floor
- If the dice gives 6, throw again and go up the number of floors that you throw

Add clumsiness : a chance of 0.1% that you will fall and will have to start all over again at floor 0.

**Suggestions** :
- Define functions for : 
    - rolling the dice
    - being clumsy
    - moving floors
    - doing one walk up the ESB
    - doing n walks up the ESB
- Use numpy arrays to keep track of success in each of the 500 walks
- Use a **seed** of 42 in order to have reproductible results (check out the function `np.random.seed`)

Please calculate :
- The mean floor you will reach on your 500 walks after throwing the dice 100x
- The probability of reaching at leats floor 60
- The probability of reaching the top floor during the game (the Empire State Building has 102 floors).