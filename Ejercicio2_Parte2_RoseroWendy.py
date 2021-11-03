# -*- coding: utf-8 -*-
""""Empezando a trabajar con Python_Ejercicio 2-Parte2"""

"""Desarrollar un programa que permita validar la contraseña introducida por un usuario con las 
siguientes comprobaciones:
 Debe contener al menos una letra minúscula entre las letras: a,b,c,d,e,f,g,h,i,j.
 Debe contener al menos una letra mayúscula entre las letras: K,L,M,N,O,P,Q,R,S,T.
 Debe contener al menos un número entre 0 y 9.
 Debe contener un símbolo especial entre: $,%,*,@
 Tamaño mínimo de 5 caracteres y máximo de 15.
Se debe solicitar la contraseña al usuario, así como informarle sobre estos requisitos para su 
contraseña, una vez validada mostrar un mensaje al usuario informándole al respecto."""

def revisar_clave(clave):
    List1=["a","b","c","d","e","f","g","h","i","j"]
    List2=["K","L","M","N","O","P","Q","R","S","T"]
    List3 =["$", "%", "*", "@"]
    val = True
      
    if len(clave) <= 4: 
        print('La longitud de la contraseña debe ser como mínimo 5 caracteres') 
        val = False
    if len(clave) > 15: 
        print('La longitud de la contraseña debe ser como máximo 15 caracteres') 
        val = False
    if not any(var in List1 for var in clave): 
        print("La contraseña debe contener al menos una letra minúscula de la lista: (a,b,c,d,e,f,g,h,i,j)") 
        val = False
    if not any(var in List2 for var in clave): 
        print("La contraseña debe contener al menos una letra mayúscula de la lista: (K,L,M,N,O,P,Q,R,S,T)") 
        val = False
    if not any(var.isdigit() for var in clave): 
        print("La contraseña debe contener al menos un número del 0 al 9") 
        val = False
    if not any(var in List3 for var in clave): 
        print("La contraseña debe contener al menos un caracter de la lista: ($,%,*,@)") 
        val = False
    if val: 
        return val 
  
def validar(): 
    clave = input("Ingresar contraseña:")
   
    if (revisar_clave(clave)): 
        print("CLAVE VÁLIDA_PUEDE CONTINUAR") 
    else: 
        print("Clave NO válida") 
          
if __name__ == '__main__': 
    validar() 