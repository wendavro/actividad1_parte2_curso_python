# -*- coding: utf-8 -*-
def ejercicio2_1():
    """"Empezando a trabajar con Python_Ejercicio 2-Parte1"""
    
    """Considerando la siguiente tupla codifique un programa que permita separar los números pares 
    e impares. También, identifique y muestre en pantalla los posibles valores que considere 
    atípicos a ese arreglo."""
    
    #PARA FILTRO DE NUMEROS PARES
    def pares_filtro(num_pares):
        pares = []
        
        for x in num_pares:
            if x % 2 == 0:
                pares.append(x)
                
        return pares
    
    Datos_2021 = (15, 20, 3,91,4, 5, 6, 7,100,91,110,900,21,33,32, 2, 4,8,10,13,13,16,15,1302)
    numeros_pares = pares_filtro(Datos_2021)
    print(f"Dada la tubpla: {Datos_2021}. \nLos numeros pares son :", numeros_pares)
    
    #PARA FILTRO DE NUMEROS IMPARES
    def impares_filtro(num_impares):
        impares = []
        
        for n in num_impares:
            if n % 2 != 0:
                impares.append(n)
                
        return impares
    
    numeros_impares = impares_filtro(Datos_2021)
    print("Los numeros impares son :", numeros_impares)
    
    #PARA FILTRO DE NUMEROS ATIPICOS A CRITERIO PERSONAL
    p=[Datos_2021[i] for i in range(len(Datos_2021)) if not i == Datos_2021.index(Datos_2021[i])]
    print(f"A mi criterio los valores atípicos son los números repetidos, \nlos cuales son:{p}")

