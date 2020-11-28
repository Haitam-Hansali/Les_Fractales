# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 14:43:55 2020

@author: Hansali haitam
"""

#EXERCICE_2:

import matplotlib.pyplot as plt
import random

X =[0.5]
Y =[0]

for i in range(30000):
    r =random.uniform(0,1)
    
    if 0 <= r <= 0.02:
        Xf = 0.5 
        Yf = 0.27* Y[i] 
    elif 0.02 <= r <= 0.17:
        Xf = -0.139* X[i] + 0.263* Y[i] + 0.57
        Yf = 0.224* Y[i] - 0.036 + 0.246* X[i]   
    elif 0.17 <= r <= 0.3:   
        Xf = 0.17* X[i] - 0.215* Y[i] + 0.408
        Yf = (0.176* Y[i]) + (0.222* X[i]) + 0.0893
    elif 0.3 <= r <= 1:
        Xf = 0.781* X[i] + 0.034* Y[i] + 0.1075
        Yf = 0.739* Y[i] - 0.032* X[i] + 0.27    
        
    X.append(Xf)
    Y.append(Yf)       
        
ax =plt.gca()
ax.set_xticks([])
ax.set_yticks([])        
plt.plot(X,Y,'g.')
plt.show()