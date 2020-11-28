# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 14:27:40 2020

@author: Hansali haitam
"""

#EXERCICE_1:

import matplotlib.pyplot as plt
import random

X =[0.5]
Y =[0]

for i in range(30000):
    r =random.uniform(0,1)
    
    if 0 <= r <= 0.1:
        Xf = 0.05* X[i]
        Yf = 0.6* Y[i] 
    elif 0.1 <= r <= 0.2:
        Xf = 0.05* X[i]
        Yf = 1 - (0.5* Y[i])    
    elif 0.2 <= r <= 0.4:   
        Xf = 0.46* X[i] - 0.32* Y[i]
        Yf = (0.38* Y[i]) + (0.39* X[i]) + 0.6 
    elif 0.4 <= r <= 0.6:
        Xf = 0.47* X[i] - 0.15* Y[i]
        Yf = (0.42* Y[i]) + (0.14* X[i]) + 1.1       
    elif 0.6 <= r <= 0.8:
        Xf = 0.43* X[i] + 0.28* Y[i]
        Yf = (0.45* Y[i]) - (0.25* X[i]) + 1.0
    elif 0.8 <= r <= 1:
        Xf = 0.42* X[i] + 0.26* Y[i]
        Yf = (0.31* Y[i]) - (0.35* X[i]) + 0.7
        
    X.append(Xf)
    Y.append(Yf)       
        
ax =plt.gca()
ax.set_xticks([])
ax.set_yticks([])        
plt.plot(X,Y,'g.')
plt.show()