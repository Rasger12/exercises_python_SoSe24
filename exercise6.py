# -*- coding: utf-8 -*-
"""
Created on Fri May  3 17:12:32 2024

@author: s_buageilasalman19
"""

a = 1
r = 0.5
s= 0
k = 0

while True:
    s +=a * r**k
    k += 1
    print (s, end = " ")
    if k > 20:
        break

