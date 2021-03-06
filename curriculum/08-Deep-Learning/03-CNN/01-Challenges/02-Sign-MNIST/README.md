# Challenge - Sign MNIST

![](https://storage.googleapis.com/kagglesdsdata/datasets/3258/5337/amer_sign2.png?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=databundle-worker-v2%40kaggle-161607.iam.gserviceaccount.com%2F20210125%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210125T052853Z&X-Goog-Expires=172799&X-Goog-SignedHeaders=host&X-Goog-Signature=081f680828ed7e9fc4f71e2f5ef026ba4090b6a6b6e84230babf407067cfb8634564b8c2a5fee3825db048050c4ad9683190556f65f55a8fd2827bf06e762ea39acac875307c9b6e875c14f6ac54870f90adb3a649e5125fa7a6d9c32ac68d5361dcb36d204a0146fcf0d70ef7e1adf7347c4c2c6ff92e51f117099c27bdf9f5a7bbe49dba110a15d856c495504f3f985f6cee707b653b2ce0f505d9290592a7992c2d690923bceab74792307b39bd53c36f49e80a4836c14364732793f3defb483259c3ec871fb60200188de86309182d7c5bc847fc3a6a53ded6e5c2ee2cef79dbb4be225272b4036f5ad5fa53d7c709ea7740afa66800a0a22f85cb61eb82)

# Context

The original MNIST image dataset of handwritten digits is a popular benchmark for image-based machine learning methods but researchers have renewed efforts to update it and develop drop-in replacements that are more challenging for computer vision and original for real-world applications.

To stimulate the community to develop more drop-in replacements, **the Sign Language MNIST** presented here follows the same CSV format with labels and pixel values in single rows. The American Sign Language letter database of hand gestures represent **a multi-class problem with 24 classes of letters (excluding J and Z which require motion).**

## The dataset

The dataset format is patterned to match closely with the classic MNIST. Each training and test case represents a label (0-25) as a one-to-one map for each alphabetic letter A-Z (and no cases for 9=J or 25=Z because of gesture motions). The training data (27,455 cases) and test data (7172 cases) are approximately half the size of the standard MNIST but otherwise similar with a header row of label, pixel1,pixel2….pixel784 which represent a single 28x28 pixel image with grayscale values between 0-255.

> You can find more informations and download the train and test sets on Kaggle : https://www.kaggle.com/datamunge/sign-language-mnist


## Guidelines

The objective of this project is to train a classifier to recognize the hand sign on each image.

⚠️ **Use Google colab for this project.**

You are largely free to follow your own heart in conducting this project. Nevertheless, here are some indications that can help you :

- **Don't forget to explore the data** : display some images and their labels, explore the distribution of classes in the train set, etc.
- **Use the [ImageDataGenerator](https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html) from Keras to practice some data augmentation** : it can help you avoid overfitting and lets you generate more data to train your model.
- You can start by trying the **classic Net5 architecture** on this dataset, and tweaking it depending on your results.
- Whatever the performance of your model (even if it is excellent !), **explore the predictions** : display some test images with the true label and the predicted label, and display the confusion matrix of your model.