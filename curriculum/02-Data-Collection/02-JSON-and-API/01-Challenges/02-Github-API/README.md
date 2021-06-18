# Challenge - Github API

![](https://dyw7ncnq1en5l.cloudfront.net/optim/news/75/75755/-c-github.jpg?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1489&q=80)

## Objectives

GET requests with Github API

## Guidelines

The Github API url is https://api.github.com. You will need to request the API using the following endpoint : `https://api.github.com/repos/{owner}/{repo}`.

- Write a function `get_description(owner, repo)` to retrieve the description of any given repository and returns it as a dictionary with the shape `{repo_name: description}`.
```
#Example : 
get_description("tensorflow", "datasets")
>>> {'datasets': 'TFDS is a collection of datasets ready to use with TensorFlow, Jax, ...'}
```

- Write a function `save_description(description, repo)` storing a given description in a `repo.json` file located in the `output` folder
- Create a list of 10 public Github repositories (you can browse the [Explore](https://github.com/explore) menu on github.com to find some inspiration). Generate a dictionnary mapping those repos to their number of subscribers. Save your work in a `followers.json` file.

Your code must be written in `src/github.py`. If needed, your can find the Github API documentation [here](https://developer.github.com/v3/).