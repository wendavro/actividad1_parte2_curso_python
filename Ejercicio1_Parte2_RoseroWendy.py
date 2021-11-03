# -*- coding: utf-8 -*-

def ejercicio1_2():
    """"Empezando a trabajar con Python_Ejercicio 1-Parte2"""

    print("\n\nPrograma que identifica el tipo de dato de un valor ingresado por el usuario, \n se realizarán cinco interacciones:")
    
    #programa pide por consola que se ingrese cinco datos los cuales engrega a la salida que tipo de dato se ha guardado en memoria.
    # al quinto paso se detiene.
    
    interac = ["Primera", "Segunda", "Tercera", "Cuarta", "Quinta"]
    
    for x in interac:
        variable = input(f"{x} interacción, ingreso de un valor cualquiera:") 
        print("Este tipo de dato en Python es: \n", type(variable))
    print("¡YA NO SE HARÁN MÁS INTERACCIONES!")


