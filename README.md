# Fruit Quality Classification Project

## Introduction
This project applies the use of Image Classification to identify popular fruits and vegetables and to classify them as healthy or rotten. Fruit Quality classification can be applied in Agricultural technology and Quality Control to identify fruits that are harmful and those that are healthy. With the use of innovative tools such as this, this identification and classificaiton becomes automated and stressfree. 

## Dataset
The data used for this project was gotten from Kaggle and is credited to Muhammad Subhan. (2024). The data contains over 29000 images of 14 different fruits which were classified as healthy or rotten. The fruits and vegetables currently present in the dataset are:

|  |  |  |  |  |
|---|---|---|---|---|
| Grape | Guava | Jujube | Mango | Orange |
| Pomegranate | Potato | Strawberry | Tomato | Cucumber |
| Apple | Banana | Ballpepper | Carrot |  |


![preview](https://github.com/awojidetola/Fruit-Quality-Classification/assets/49078266/3d5d1958-e1de-4293-863f-bf9a44b83bcb)

### Transformation
The data was divided into three parts: Training Set, Validation Set and Testing Set in the ratio: 70%, 20% and 10%. The model was trained on the training data and accessed using the validation set. The test data was used to access the model performance on new data. 
The images were transformed by:
- Resizing them to a uniform size
- Vertifical and Horizontal Flip
- Converting it to tensor. 

## Modelling
The **ResNet50** model was applied to train the data using the SGD optimizer. The model has an accuracy of 91.3% on the training set and 90.99% on the test set. 


![prediction](https://github.com/awojidetola/Fruit-Quality-Classification/assets/49078266/59771c85-70a2-4ea3-a9d9-5fb78a06cdd2)

## Deployment 

## References
- Muhammad Subhan. (2024). Fruit and Vegetable Disease (Healthy vs Rotten) [Data set]. Kaggle. https://doi.org/10.34740/KAGGLE/DSV/8463025
- Koonce, B., & Koonce, B. (2021). ResNet 50. Convolutional neural networks with swift for tensorflow: image recognition and dataset categorization, 63-72.
