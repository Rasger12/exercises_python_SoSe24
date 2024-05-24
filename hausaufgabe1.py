# -*- coding: utf-8 -*-
"""
Created on Fri May  3 17:12:32 2024

@author: s_buageilasalman19
"""

AK = 10000  #Anfangskapital
SR = 1000   #Sparrate am ende des jahres
i = 1       # Zinsen in prozent
lz = 10     #Laufzeit in jahren
list= []

def spar_funktion(AK,SR,i,lz):
    for k in range(1,lz-1):
        list.append(((AK+ (1000*k))*(1+(i/100)))**k) 
    return list
        
        
        
    

print(spar_funktion(AK,SR,i,lz))