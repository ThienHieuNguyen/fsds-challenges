# Challenge - Terminal Poetry

---
![](https://images.unsplash.com/photo-1505848460926-cafbb9f7cc3f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1489&q=80)
Photo by [abi ismail](https://unsplash.com/photos/tu7g9G3J9Oo)

## Objectives
Learn to work with command lines

## Guidelines

1. Go to `~/code/YOUR_GITHUB_USERNAME/vivadata-student/curriculum/00-Basics/01-Terminal/01-Challenges/01-Terminal-Poetry` using `cd`. Check your position with `pwd`. Create a new directory called `sonnets` and move into it.

2. Pick a poem of your choice http://shakespeare.mit.edu/Poetry/sonnets.html :
   - load it in a file called `sonnet_1.txt` using `curl`;
   - use a copy paste to create another file `sonnet_2.txt` containing the text of the same poem ;
   - check the content of the two files with `cat`;
   - compare the two files with `diff`.

3. Use the `echo` command and the redirect operator `>` to make a file called `foo.txt` containing the text “hello, world".
   - using the `cp` command, make a copy of `foo.txt` called `bar`;
   - Using the `diff` command, confirm that the contents of both files are the same;
   - By combining the `cat` command and the redirect operator `>`, create a copy of `foo.txt` called `baz` without using the `cp` command;
   - Create a file called `mix.txt` containing the contents of `foo.txt` followed by the contents of `bar`.

4. Listing files :
   - List only the files starting with the letter “b”;
   - List all the non-hidden files and directories that start with the letter “s”;
   - List all the non-hidden files that contain the string “onnet”, long-form by reverse modification time.

5. Navigating directories :
   - Next to the sirectory `sonnets`, make a directory `backup` with a subdirectory `subdir`, then rename the subdirectory to `nodir`;
   - Copy all the files in `sonnets`, with directory, into `backup`;
   - Copy all the files in `sonnets`, without directory, into `nodir`;
   - Remove `backup` and everything in it using a single command.

6. **OPTIONAL**

Inspecting files :
   - By searching `man grep` for “line number”, construct a command to find the line numbers in `sonnets_2.txt` where the string “is” appears.
   - Figure out how to go directly to the last occurrences of “is” when running `less sonnets_2.txt`;
   - By piping the output of `grep` to `head`, print out the first (and only the first) line in `sonnets_2.txt` containing “is”.
