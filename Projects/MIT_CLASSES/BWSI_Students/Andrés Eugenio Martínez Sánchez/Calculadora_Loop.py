# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# te pide un input y luego imprime 

from math import sqrt

y=True
while y: 

 A = float(input("Enter number: ")) 
 B = float(input("Enter number: "))
 C = float(input("Enter number: "))

 

 if ((B**2)-4*A*C) < 0:
    
      print("La solución de la ecuación es con numeros complejos")
      
 elif ((B**2)-4*A*C) >= 0:
    
     x1 = (-B+sqrt(B**2-(4*A*C)))/(2*A)
     x2 = (-B-sqrt(B**2-(4*A*C)))/(2*A)
      
     str(x1)
     str(x2)
    
     print (x1)
     print (x2)
    
 X = input("Do you want to make another? ")
 print (X)
    
 yes = True
 
 if X == "yes":
     y == True
     
      
 elif X == "exit" or "no":
     print ("come back soon")
     break
     
 
    
    
    
    
"""     
 elif X == "no":
     
     print ("come back soon")
     break
"""
    

#y = float(b**2 (- 4 * a+c))
#z = float (b**1/2)

#x1 = float (-b +z)
#2 = float (-b -z)


#print (float(x1/ (2*a), x2/ (2*a))

