import csv
import random
import math
import numpy as np
import pandas as pd


dataset=pd.read_csv("C:\\Users\\modak\\Downloads\\IPL.csv")



x = dataset.iloc[:, 7:-1].values
y = dataset.iloc[:, -1].values

one = np.ones((len(x), 1))
x = np.append(one, x, axis=1)

y = np.array(y).reshape((len(y),1))
print(y.shape)

def train_test_split(x, y, split):

    #randomly assigning split% rows to training set and rest to test set
    indices = np.array(range(len(x)))
    
    train_size = round(split * len(x))

    random.shuffle(indices)

    train_indices = indices[0:train_size]
    test_indices = indices[train_size:len(x)]

    x_train = x[train_indices, :]
    x_test = x[test_indices, :]
    y_train = y[train_indices, :]
    y_test = y[test_indices, :]
    
#print(x_train)

    return x_train,y_train, x_test, y_test

split = 0.7
X_train, Y_train, X_test, Y_test = train_test_split(x, y, split)
print(X_train)
print(Y_train)
print(X_test)
print(Y_test)


def normal_equation(x, y):
    beta = np.dot((np.linalg.inv(np.dot(x.T,x))), np.dot(x.T,y))

    return beta
def predict(X_test, beta):
    return np.dot(X_test, beta)


def dfs(r,):

beta = normal_equation(X_train, Y_train)
predictions = predict(X_test, beta)
prediction =predict([[1,49,3,6.4,43,0,21,2]],beta)

print(prediction)


def metrics(predictions, Y_test):

    #calculating mean absolute error
    MAE = np.mean(np.abs(predictions-Y_test))

    #calculating root mean square error
    MSE = np.square(np.subtract(Y_test,predictions)).mean() 
    RMSE = math.sqrt(MSE)

    #calculating r_square
    rss = np.sum(np.square((Y_test- predictions)))
    mean = np.mean(Y_test)
    sst = np.sum(np.square(Y_test-mean))
    r_square = 1 - (rss/sst)
    

    return MAE, RMSE, r_square


mae, rmse, r_square = metrics(predictions, Y_test)
print("Mean Absolute Error: ", mae)
print("Root Mean Square Error: ", rmse)
print("R square: ", r_square)
