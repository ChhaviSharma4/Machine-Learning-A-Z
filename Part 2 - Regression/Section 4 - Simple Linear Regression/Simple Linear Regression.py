# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Simple Linear Regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting results
y_pret = regressor.predict(X_test)

# Plotting Training stuff
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train , regressor.predict(X_train), color =  'blue')
plt.title('Salary vs Exp (Training Set)')
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.show()

# Plotting Test Set
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train , regressor.predict(X_train), color =  'blue')
plt.title('Salary vs Exp (Test Set)')
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.show()

