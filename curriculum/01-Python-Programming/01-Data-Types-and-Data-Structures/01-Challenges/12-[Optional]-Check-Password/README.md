# Challenge - Check Password

![](https://images.unsplash.com/photo-1549927455-67cc16cc490c?ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80)

A website requires the users to input username and password to register. Write a program to check the validity of password input by users.

Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12

Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.

Example
If the following passwords are given as input to the program:
`ABd1234@1,a F1#,2w3E*,2We3345`
Then, the output of the program should be:
`ABd1234@1 is a valid password
a F1# is an invalid password
2w3E* is an invalid password
2We3345 is an invalid password`
