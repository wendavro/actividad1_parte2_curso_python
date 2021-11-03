# -*- coding: utf-8 -*-
from Ejercicio4.Ejercicio1_Parte1_RoseroWendy import ejercicio1_1
import Ejercicio4.Ejercicio1_Parte2_RoseroWendy as ej1_2
import Ejercicio4.Ejercicio2_Parte1_RoseroWendy as ej2
import Ejercicio4.Ejercicio2_Parte2_RoseroWendy as ej2_2
import Ejercicio4.Ejercicio3__Parte1_RoseroWendy as ej3
menuprincipal=int(input("Menú Principal de los programas que se desea ejecutar: \n1: Ejercurtar tipo de valores \
                        \n2: Tipo de valor ingresado por teclado\
                        \n3: Dada una tupla identificar valores: pares,impares, atípicos\
                        \n4: Validación de clave\
                        \n5: Valores altos y bajos de diccionarios desplegados en menús y submenús\
                        \n6: Salir \nElija una opción:"))
while menuprincipal != 0:
  try:
        if menuprincipal == 1:
            print("Primera opción - Ejercurtar tipo de valores ")
            ejercicio1_1()
        elif menuprincipal == 2:
            print("Segunda Opción - Tipo de valor ingresado por teclado")  
            ej1_2.ejercicio1_2()
        elif menuprincipal == 3:
            print("Tercera opción - Dada una tupla identificar valores: pares,impares, atípicos")  
            ej2.ejercicio2_1()
        elif menuprincipal == 4:
            print("Cuarta opción - Validación de clave") 
            ej2_2.validar()
        elif menuprincipal == 5:
            print("Quinta opción - Valores altos y bajos de diccionarios desplegados en menús y submenús")                            
            ej3.valores_alto_bajos()
        elif menuprincipal == 6:
            print("Fin")
            break
        
        else:
            print("Seleccione la opción correcta")
        
        menuprincipal=int(input("Menú Principal de los programas que se desea ejecutar: \n1: Ejercurtar tipo de valores \
                            \n2: Tipo de valor ingresado por teclado\
                            \n3: Dada una tupla identificar valores: pares,impares, atípicos\
                            \n4: Validación de clave\
                            \n5: Valores altos y bajos de diccionarios desplegados en menús y submenús\
                            \n6: Salir \nElija una opción:"))
      #pass
  except Exception:
      pass
  finally:
      pass
   
