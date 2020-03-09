#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 13:49:48 2020

@author: andres
"""

from math import sqrt

A = float(input("Enter number: ")) 
B = float(input("Enter number: "))
C = float(input("Enter number: "))

 

if ((B**2)-4*A*C) < 0:
    
      print("La solución de la ecuación es con numeros complejos")
      
elif ((B**2)-4*A*C) >= 0:
    
     x1 = (-B+sqrt(B**2-(4*A*C)))/(2*A)
     x2 = (-B-sqrt(B**2-(4*A*C)))/(2*A)
      
  
     print (x1)
     print (x2)

    