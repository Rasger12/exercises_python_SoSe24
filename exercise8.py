# -*- coding: utf-8 -*-
"""
Created on Fri May  3 17:12:32 2024

@author: s_buageilasalman19
"""

def vokon_zählen(wort):
    V = ["a"," e", "i", "o", "u"]
    K = ["q" ,"w" ",r", "t", "z", "p", "ü", "s", "d", "f", "g", "h", "j" , "k", "l", "ö", "ä", "y", "x", "c", "v", "b", "n", "m"]
    Vc = 0
    Kc = 0
    for i in wort:
        if i in V:
            Vc += 1 
        if i in K:
            Kc += 1 
    print("Es gibt " + str(Vc) + " Vokale und " + str(Kc) + "Konsonanten")
    
    
    

            


