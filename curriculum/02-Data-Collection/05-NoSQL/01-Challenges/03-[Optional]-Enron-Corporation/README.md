## Challenge - ENRON Corporation ✉️


![](https://images.unsplash.com/photo-1527259216948-b0c66d6fc31f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=40)

---

## Instructions

This time we will deal with a dataset containing some email exchanges of ENRON Corporation. You will find the dataset in this folder named `enron.json`. This time we'll be using **Pymongo.**

### I. First Hand

- Load the `enron.json` data into `vivadata` dataset and name the collection `emails`.

- Connect to the collection using **Pymongo**.

- Import the prettify printer.

- Explore the structure of 3 documents.

- Count the total number of emails.

### II. Reporting Communication

- What are the list of existing folders?

- Number of emails per type of folder.

- The number of emails sent by each user in a descending order.

- Number of emails received by email as a direct email and not a CC in a descending order.

- Give both the naive total number of words contained in the subject by sender and the number of words to subject ratio for each sender in a descending order (based on the ratio). Naive means using a space split.

- All IDs of emails sent to a `@hotmail.com` address directly or using a CC in `sent` folder.

### III. Corrections

- Remove `rosalee.fleming@enron.com` from all the email recipients (CC not considered).
- Add `rob.bradley@enron.com` to the list of recipients to all the mails sent by `rosalee.fleming@enron.com`.
