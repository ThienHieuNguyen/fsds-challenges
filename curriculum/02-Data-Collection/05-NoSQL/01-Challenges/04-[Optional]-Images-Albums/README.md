## Challenge - Images & Albums 📷


![](https://images.unsplash.com/photo-1502613374390-8da7aa532177?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1352&q=40)

---

## Instructions

This time we will work with two collections, one containing a list of images (height, width, and tags) and the other one containing a list of albums where each album refers to a list of image IDs contained in the image collection. In NoSQL databases it is best to not use "join logic", so the objective here is to use **Python** to create a new collection where we have nested documents so albums will contain the detailed information for each image it contains. The two datasets are in this same folder : `images.json` and `albums.json`.

### I. Data Discovery

- Load the two datasets in a new database named `palbum` into two collections `images` and `albums`.

- Connect to both collections.

- Try to understand the data structure of the `albums` collection and the `images` collection.

### II. Migration

- Write a Python script That will create a new collection named `albums-rich` , this collection will contain the same data as `albums` and instead of having images IDs we will have the corresponding images documents.

  If we have an album document like :

  ```
  {'_id': 3,'images': [8, 17]}
  ```

  In our new collections it must be like this :

  ```
  {
  	'_id': ObjectId('587425467235997423684'),
   	'images': [ 
   				{'height': 480, 'width': 640, 'tags': ['kittens', 'travel']},
   				{'height': 480, 'width': 640, 'tags': ['car']}
   			  ]
  }
  ```


- By using the **MongoDB** official documentation try to create a `BSON` dump of the newly created collection.

- Drop the new created collection `albums-rich`.

- Reload `albums-rich` by using the generated `BSON` file. 

### III. The greatest Tag!

- By using `album-rich`, what are the 10 most used tags in albums ? and what it is the number of albums for each tag ? Is there something odd, if it's the case what is it ?
