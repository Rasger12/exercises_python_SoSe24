# -*- coding: utf-8 -*-
"""
Created on Fri May 31 12:25:59 2024

@author: s_buageilasalman19
"""
import matplotlib.pyplot as plt


def buchstaben_häufigkeit(x):
    mein_d = {}
    for buchstabe in x.lower():
        if buchstabe.isalpha():
            if buchstabe not in mein_d:
                mein_d[buchstabe] =1
            else:
                mein_d[buchstabe] += 1
    mein_d_sorted = dict(sorted(mein_d.items()))
    
    return mein_d_sorted

bh_dict = buchstaben_häufigkeit(x = "Wie gehtxxx es 445Ihnen")

plt.bar(bh_dict.keys(), bh_dict.values())

