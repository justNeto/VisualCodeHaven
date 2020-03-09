#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 17:23:40 2020

@author: andres
"""

x = input("introduce una cadena de texto: ")

y = len(x)


if y >= 3 and y <= 10:
    print ("Todo cool")
    
elif y < 3 or y > 10:
    print ("Todo mal")


