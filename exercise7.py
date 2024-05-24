# -*- coding: utf-8 -*-
"""
Created on Fri May  3 17:12:32 2024

@author: s_buageilasalman19
"""

def buchstaben_zählen(input):
    x = ""
    for buchstabe in input:
        if buchstabe.isalpha()== True:
            x+= buchstabe
            
        
    
    print(len(x)   )


