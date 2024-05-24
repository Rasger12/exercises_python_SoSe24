# -*- coding: utf-8 -*-
"""
Created on Fri May  3 17:12:32 2024

@author: s_buageilasalman19
"""



import numpy as np



x = np.arange(1,13)

x = x.reshape(2,3,2 )

#print(x)

#Aufgabe:

m = np.identity(5) 
m[0:2,3:5] = 3
m[3:5,0:2] = 2

n = np.eye(5, dtype= "int")
n[0:2,3:5] = 3
n[3:5,0:2] = 2
n[2:4] = n[2:4]*5