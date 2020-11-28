# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 14:59:37 2020

@author: Hansali haitam
"""

#EXERCICE_3:

import matplotlib.pyplot as plt
import random

X =[1, 7, 1, 3]
Y =[1, 2, 9, 3]

for i in range(15000):
    r =random.uniform(0,1)
    
    if 0 <= r <= 1/3 :
        X.append((X[i+3] + X[0]) /2)
        Y.append((Y[i+3] + Y[0]) /2)
    elif 1/3 <= r <= 2/3:
        X.append((X[i+3] + X[1]) /2)
        Y.append((Y[i+3] + Y[1]) /2) 
    elif 2/3 <= r <= 1:          
        X.append((X[i+3] + X[2]) /2)
        Y.append((Y[i+3] + Y[2]) /2)       
        
ax =plt.gca()
ax.set_xticks([])
ax.set_yticks([])        
plt.plot(X,Y,'g.')
plt.show()