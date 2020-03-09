# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 14:37:17 2020

@author: Alonso
"""
cal = raw_input("Insert grade: ");

def numChecker (grade):
    return any(char.isalpha() for char in grade);

if numChecker(cal):
    print ("Not a numeric grade");

else: 
    cal = int(cal);
    if cal > 100 or cal < 0:
        print("Not a valid grade");
    elif 100 >= cal >= 96:
        print("OMG :O");
    elif 95 >= cal >= 86:
        print("Incredible");
    elif 85 >= cal >= 76:
        print("Good");
    elif 75 >= cal >= 70:
        print("That was close");
    else:
        print("You failed :(");
        
    
