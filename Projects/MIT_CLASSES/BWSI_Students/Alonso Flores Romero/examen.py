# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 17:02:29 2020

@author: AL
"""
import numpy as np
import matplotlib.pyplot as plt
a = np.array([[1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
            [1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
            [1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,0,0,1,1,1,1,1],
            [1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,0,1,1,1,1],
            [1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1],
            [1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,0,1,1,1],
            [1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1],
            [1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,0,1,0,0,1],
            [1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,1,1,1,0,0,0,1,0,1],
            [1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,1,0,0,0,1,0,0],
            [1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,0,0,1,1,0,0,0,1,0,0],
            [1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,0,0,1,1,0,0,0,1,0,0],
            [1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,0,0,1,1,1,0,0,1,1,0],
            [1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,1,1,1,0],
            [0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,1,1,1,1,0,0,1,0,1,1,1,1,1,1,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,0,0,0,0,1,0,0],
            [1,1,0,0,0,0,0,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,0,1,0],
            [1,1,1,0,0,0,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,1,1,0,0,0,0,0,0,1,0,0],
            [1,1,0,0,0,0,1,1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,1,1,1,0,0,0,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0],
            [1,1,1,1,0,0,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1],
            [1,1,1,1,1,0,0,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1],
            [1,1,1,1,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,0,1,1],
            [1,1,1,1,1,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1],
            [1,1,1,1,1,1,1,0,0,1,1,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1,0,0,1,1,1],
            [1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,0,0,1,0,0,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0,0,1,0,0,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1]])

#Código para checar 1
for i in range(34):
    print(a[i])


print("             ");

 
#Código para intercambiar colores   

#Creo un loop que me permita pasar por todos los valores equivalentes a cada fila.
for i in range(34):
    #Guardo los valores en esta variable para poder referirme a través de esta al número de fila
    checker = i;
    #Creo un loop mas para pasar por todos los valores equivalentes a cada columna.
    for i in range(34):
        #Checho con esta condicional si el valor de tal columna en tal fila es igual a 1 o a 0, y en caso de que sea 1 lo paso a 0, y en caso de que sea 0 lo paso a 1.
        if a[checker][i] == 1:
            a[checker][i] = 0;
        elif a[checker][i] == 0:
            a[checker][i] = 1;
 
#Código para reflejar en X o Y

#Código para reflejar en X
            
#Creo un loop que me permita pasar por todos los valores equivalentes a cada fila.
for i in range(34):
      #Guardo los valores en esta variable para poder referirme a través de esta al número de fila
      deter = i;
      #Creo un loop mas para pasar por todos los valores equivalentes a cada columna.
      for i in range(34):
          #Ahora que tengo mis coordenadas, hago que cada valor se iguale primero el ultimo equivalente en la fila por asi decirlo con el primero equivalente en la fila y luego visceversa.
          a[deter][34-i] = a[deter][i];
          a[deter][i] = a[deter][34-i];

#Código para reflejar en Y
          
#Creo un loop que me permita pasar por todos los valores equivalentes a cada fila.
for i in range(34):
      #Guardo los valores en esta variable para poder referirme a través de esta al número de fila
      deter = i;
       #Creo un loop mas para pasar por todos los valores equivalentes a cada columna.
      for i in range(34):
          #Ahora que tengo mis coordenadas, hago que cada valor se iguale primero el ultimo equivalente en la fila por asi decirlo con el primero equivalente en la fila y luego visceversa.
          a[34-i][deter] = a[i][deter];
          a[i][deter] = a[34-i][deter];
       
#Código para checar 2
for i in range(34):
    print(a[i])