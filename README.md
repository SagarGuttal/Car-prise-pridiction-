# Car Prise Prediction
## Description
> Determining whether the listed price of a used car is a challenging task, due to the many factors that drive a used vehicle’s price on the market. The focus of this project is developing machine learning models that can accurately predict the price of a used car based on its features, in order to make informed purchases.I implement and evaluate various learning methods on a dataset consisting of the sale prices of different makes and models across cities in the India with respect of year of which car was purchase. Our results show that Random Forest model is best among all the model

## Motivation for this project 
> Deciding whether a used car is worth the posted price when you see listings online can be difficult.Several factors, including car model, kilometer driven, year of purchased, etc. can influence the actual worth of a car. From the perspective of a seller, it is also a dilemma to price a used car appropriately[2-3]. Based on existing
data, the aim is to use machine learning algorithms to develop models for predicting used car prices.

## Steps are taken to this Project :-
1. About Dataset
2. Data preprocessing
3. Feature engineering
4. Model-Building/Hyperparameter Tuning
5. Model Evaluation:
6. Creating front end UI for a website
7. Creating backend using python

## Tools and Technique
- Language :- Python
- Python libraries :- Numpy, Pandas, Sklearn, Matplot, Seaborn

## About Dataset
- In this project i taken dataset from CarDekho.com comapany which is India's leading car search venture that helps users buy cars that are right for them.
- The data set contains about 301 cars information and there prises. 
- link of dataset = https://www.kaggle.com/datasets/pradeep8896/car-pricecar-dekho

## Data preprocessing
- Checking the null values.
- Checking the unique values in each columns.
- Creating new feature column - No of years column.
- Droping irrevelent columns in final datset.

> Final data
![](https://github.com/SagarGuttal/Deployment-of-model-in-website/blob/main/Finaldf.png)
## Feature engineering
- Above preprocessed dataset contains categorical values thats why converted into numarical values using pandas get_dummies methode
- Selecting best feature columns for creating a model
- Image for top features thats are helping to creat a best model for our project

![](https://github.com/SagarGuttal/Deployment-of-model-in-website/blob/main/Top%20features.png)

- Checking distribution of data points in each columns.
- Checking colinearity among the columns and visualy anlyses the co-relation between the columns using Heat maps
- Split out data into feature columns(X) and target column(y) 
- Taking 80% of the data for training and remaning 20% data for testing

## Model building
- In our model building i taken ensembling technique algorithms - Random forest, Gradient boosting, Adaboost regressor for training our model
- Taking all model for training and checking each model performance based on MSE(Mean Squared Error) and R_2 score.
- Taking one best performing model or less error and more R_2 score model.
- Improving the model performance by tunning the parameters or we call it as Hyperparameter tunning.
- In hyperparameter taking random values and using Cross validation technique for reducing Overfitting problems in our model
- finally selecting tunnned parameters and again trained the model and check the performace 
- In this project i taken Random forest algorithm based on its performance and got 92 % accuracy.

- Model performance
![](https://github.com/SagarGuttal/Deployment-of-model-in-website/blob/main/model%20performance.png)

-Distibution of error values 
![](https://github.com/SagarGuttal/Deployment-of-model-in-website/blob/main/MSE%20distrubution.png)
