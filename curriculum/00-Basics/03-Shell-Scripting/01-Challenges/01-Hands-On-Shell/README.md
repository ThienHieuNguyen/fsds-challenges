# Challenge - Hands on shell

![](https://images.unsplash.com/photo-1480506132288-68f7705954bd?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1693&q=80)


## 1.1. Creating a bash script

- Let's create a script which reads the first line of all csv files in the current directory
- Save this script as headers.sh
- Make sure your script is **executable** (`chmod` command)
- Execute your file with : `./headers.sh`


## 1.2. More bash scripting

- Let's create a script that lists all the folders and directories in the current directory whose name starts with a `P`
- Save this script as list.sh
- Make sure your script is **executable** (`chmod` command)
- Execute your file with : `./list.sh`


## 1.3. Desktop cleaning

If you're like me, you will have encountered this issue : I often find my computer desktop extremely messy, full of random pictures. Let's clean that up !

- Let's create a script that will :
    - make a directory named `pictures` in your `Desktop`
    - move all images (extensions `.png` or `.jpg`) in your `Desktop` into `pictires`
- Save this script as cleanup.sh
- Make sure your script is **executable** (`chmod` command)
- Execute your file with : `./cleanup.sh`



# 2. Working with arguments

Let's create a file `arguments.sh` that will print to the console how many arguments were given when executing the script.


# 3. Working with conditions

Write a shell script that prompts the user for a name of a file or directory and reports if it is a regular file, a directory, or another type of file. 

Also perform an `ls` command against the file or directory with the long listing option.

**Then**, modify the previous script so that it accepts the file or directory name as an argument instead of prompting the user to enter it.