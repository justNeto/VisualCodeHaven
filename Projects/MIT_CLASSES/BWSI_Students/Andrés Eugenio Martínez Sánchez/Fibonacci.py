#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 15:38:39 2020

@author: andres
"""

"""Hacer un programa que te devuelva un término específico de la 
secuencia de Fibonacci. El usuario tiene escoger el término.
Los dos primeros términos son 1."""

a= 1
b = 1

n = int(input("Enter anumber: "))

for i in range(n):

   a, b = b, a + b
   x = [a]
   y = x[-1]
    
   print(y)    
    
    
     