# -*- coding: utf-8 -*-
"""
Created on Fri May  3 17:12:32 2024

@author: s_buageilasalman19
"""

meine_liste = [3,5,2,3]
def steigung_funktion(liste):
    # Steigungsformel m=Steigung/Verlauf= y2-y1/x2-x1
    x1= liste[0]
    x2= liste[1]
    y1= liste[2]
    y2= liste[3]
 
    if y2-y1 == 0 or x2-x1 ==0:
        return "Die Steigung ist nicht definiert."
    else:
        return (y2-y1)/(x2-x1)
    
    
    
    
    # days = ["monday", "Dienstag", "Mi", "Do", "Fr", "Sa", "So"]
    # days_german = days[:]

    # days_german[6] = "Sonntag"
 


# '>>> städte = ["Rome", "Paris", "London", "Berlin"]
# >>> städte
# ['Rome', 'Paris', 'London', 'Berlin']
# >>> index("Berlin")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'index' is not defined
# >>> index(städte("Berlin"))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'index' is not defined
# >>> städte.index("Berlin")
# 3
# >>> städte.pop(3)
# 'Berlin'
# >>> städte
# ['Rome', 'Paris', 'London']
# >>> städte.append("Madrid")
# >>> städte
# ['Rome', 'Paris', 'London', 'Madrid']
# >>> städte.insert(1, "Amsterdam")
# >>> städte
# ['Rome', 'Amsterdam', 'Paris', 'London', 'Madrid']
# >>> städte.sort
# <built-in method sort of list object at 0x00000260AA470F00>
# >>> städte.sort()
# >>> städte
# ['Amsterdam', 'London', 'Madrid', 'Paris', 'Rome']
# >>>'