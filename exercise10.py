# -*- coding: utf-8 -*-
"""
Created on Fri May  3 17:12:32 2024

@author: s_buageilasalman19
"""



import numpy as np

d = np.arange(1,11)
D = np.tile(d,(10,1) )


D_sum =D.sum(axis = 0)
D_mean =D.mean(axis = 1)



print(D)
print(D_sum)
print(D_mean)


