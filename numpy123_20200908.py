# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 11:40:23 2020

@author: 23645
"""

import numpy as np

def npSum():
    a = np.array([0, 1, 2, 3, 4])
    b = np.array([9, 8, 7, 6, 5])
    
    c = a**2 + b**3
    
    return c

print(npSum())
