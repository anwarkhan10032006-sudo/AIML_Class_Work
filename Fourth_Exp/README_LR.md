# Implementation of simple and multiple regression
This experiment implements simple, multiple, and polynomial regression models to predict output values and evaluates their performance using R², MAE, and RMSE metrics.
--- 

# Pseudocode 
```
Start

Create dataset with X1, X2, and Y values

Convert dataset into table format

Select:
    X_simple = X1
    X_multiple = X1 and X2
    y = Y

----------------------------------
Simple Linear Regression
----------------------------------
Create Linear Regression model
Train model using X_simple and y

----------------------------------
Multiple Linear Regression
----------------------------------
Create Linear Regression model
Train model using X_multiple and y

----------------------------------
Polynomial Regression (Degree = 2)
----------------------------------
Convert X_simple into polynomial features
Create Linear Regression model
Train model using polynomial features and y

----------------------------------
Display Results
----------------------------------
Print regression model names
Print R2, MAE, RMSE values (as per lab manual)

End


```