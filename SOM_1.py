# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 23:41:06 2023

@author: Hp
"""
#Importing the libraries

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Importing the Dataset

dataset = pd.read_csv('Credit_Card_Applications.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values
 
#Feature Scaling

from sklearn.preprocessing import MinMaxScaler 
sc = MinMaxScaler(feature_range=(0,1))
X = sc.fit_transform(X)

#Training the SOM

from minisom import MiniSom
som = MiniSom(x = 10, y = 10, input_len = 15, sigma = 1.0, learning_rate=0.5) 
som.random_weights_init(X)
som.train_random( data = X, num_iteration = 100)

#Visualising the result

from pylab import bone, pcolor, colorbar, plot, show
bone()
pcolor(som.distance_map().T)
colorbar()
markers = ['o', 's']
colors = ['r', 'g']
for i, x in enumerate(X):
    w = som.winner(x)
    plot(w[0] + 0.5, w[1] + 0.5, markers[y[i]], markeredgecolor = colors[y[i]], markerfacecolor = 'None', markersize = 10, markeredgewidth = 2)

show()

#Finding the Frauds

mappings = som.win_map(X)
frauds = np.concatenate((mappings[(8,4)], mappings[(1,4)]), axis = 0)
frauds = sc.inverse_transform(frauds)

#Printing the fraud Clients

print('Fraud Customer IDs')
for i in frauds[:, 0]:
    print(int(i))