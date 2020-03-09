#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 12:57:42 2020

@author: andres
"""

"""Crea un programa que acepte un String del usuario e
 imprima true si es un palíndromo o false si no lo es"""
 
print ("Is your word a palindrome?")
x = input("Enter a word: ")
y = x.replace(" ", "")
z = y.casefold()

reversa = z[::-1]

if reversa == z:
    print ("True")

elif reversa != z:
    print ("False")
