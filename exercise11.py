# -*- coding: utf-8 -*-
"""
Created on Fri May  3 17:12:32 2024

@author: s_buageilasalman19
"""



import numpy as np

E = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[9,8,7],[6,5,4],[3,2,1]], [[9,8,7],[6,5,4],[3,2,1]]])

E_sum = E.sum(axis= (1,2))
E_mean = E.mean(axis= (1,2))



print(E)
print("")
print(E_sum)
print("")
print(E_mean)




