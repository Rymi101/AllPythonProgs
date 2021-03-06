# -*- coding: utf-8 -*-
"""LinRegPrediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1p6zOYTn6UG7w5BMAtvnWzVMg3PLTnJtN
"""

import pandas as pd
from sklearn.model_selection import train_test_split

url = "https://raw.githubusercontent.com/gheniabla/datasets/master/score.csv" #grab scores
exams = pd.read_csv(url) #create dataframe
exams.head(15)

#create x and y values for your machine learning model
XVals = exams.iloc[:, :-1].values
YVals = exams.iloc[:, 1].values

from sklearn.model_selection import train_test_split
X_Train, X_Test, Y_Train, Y_Test = train_test_split(XVals, YVals, test_size = 4/5, random_state = 0)

#create and fit regression line
from sklearn.linear_model import LinearRegression
regress = LinearRegression()
regress.fit(X_Train, Y_Train)

#print out important values and make a guess using the regression line
print("Intercept=", regress.intercept_)
print("Slope=", regress.coef_)
exam_score = regress.predict([[8.0]])
print("Predicted Score", exam_score)