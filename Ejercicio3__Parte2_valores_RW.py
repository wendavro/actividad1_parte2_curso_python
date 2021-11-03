# -*- coding: utf-8 -*-
from heapq import nlargest #Se usó librería para acortar el proceso y el código

def valores(diccionario):
 
    print((sorted(diccionario.values())))
            
    #VALORESS ALTOS USANDO LIBRERIAS
   
    num =  int(input("Ingrese cuantos valores altos desea  (solo se permiten valores numéricos):"))
    valores_altos = nlargest(num, diccionario, key = diccionario.get)
    if num <= len(diccionario):
        for val in valores_altos:
            print(val, ":", diccionario.get(val))
            lista=[]
        for k in range(0,num):
            lista.append([])
            lista[k].append(diccionario[val])
        print("Valores calculados en formato LISTA:", lista)
        print("Valores calculados en formato TUPLA:", tuple(lista))   
    else:
        print(f"El número ingresado supera el número de registros del diccionario, \n el valor debe ser menor a {len(diccionario)}")
    
        
    #VALORES BAJOS USANDO IF-FOR
    dicc1 = sorted(diccionario.values())
    num2 = int(input("Ingrese cuantos valores bajos desea ver (solo se permiten valores numéricos):"))
    
    if num2 <= len(diccionario):
        for val in range(0,num2):
            print(dicc1[val])
        lista1=[]
        for val in range(0,num2):
            lista1.append([])
            lista1[val].append(dicc1[val])
        print("Valores calculados en formato LISTA:", lista1)
        print("Valores calculados en formato TUPLA:", tuple(lista1))
                   
    else:
        print(f"El número ingresado supera el número de registros del diccionario, \n el valor debe ser menor a {len(diccionario)}")    

    