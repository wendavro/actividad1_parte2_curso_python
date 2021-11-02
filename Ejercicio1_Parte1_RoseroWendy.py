# -*- coding: utf-8 -*-

""""Empezando a trabajar con Python_Ejercicio 1-Parte1"""

print("Realizado por: Wendy Rosero")

"""Consultando los tipos de valores:"""
num1=875
num2=4.89
dat3="Now is better than never."
num4= 1.32
num5=5 + 8j
num6= 8.2
dat7= "Readability counts."
print("Tipos de valores")
print(f"El tipo de dato de {num1} es:\n", type(num1)) #la salida entrega un tipo de dato int
print(f"El tipo de dato de {num2} es:\n",type(num2))  #la salida entrega un tipo de dato float
print(f"El tipo de dato de {dat3} es:\n",type(dat3))  #la salida entrega un tipo de dato string
print(f"El tipo de dato de {num4} es:\n",type(num4))  #la salida entrega un tipo de dato float
print(f"¿El valor {num5} corresponde a un valor entero?\n",isinstance(num5, int)) #la salida entrega un false
print(f"¿El valor {num6} corresponde a un valor entero?\n",isinstance(num6, int)) #la salida entrega un false
print(f"¿El texto: {dat7},corresponde a un string?\n",isinstance(dat7, str))  #la salida entrega un true

