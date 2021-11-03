# -*- coding: utf-8 -*-
def valores_alto_bajos():
    from Ejercicio3__Parte2_valores_RW import valores
    
    menuprincipal=int(input("Menú Principal: \n1: Demostración del cálculo de valores altos y bajos en diccionarios.\
                            \n2: Salir \nElija una opción:"))
    while menuprincipal != 0:
    
        if menuprincipal == 1:
                print("Uno")
                submenu=int(input("Submenú seleccione un diccionario:\n1){Raul:34,Paula:19,Jorge:43,Richard:10,Diana:3,Isabel:76,Gustavo:12,Diego:37} \
                                  \n2) {tplA:(4,-12,56,-34,98,102),tplB:(9,0,1,10,-3,14),tlpC:(87,12,56,987,-61)} \
                                  \n3) {val1:-12.5,val2:12.5,val3:83,val4:2.1,val5:23,val6:100,val7:13.4,val8:92} \
                                  \n4) {lst1:[4,6,-12,56,-9,5.7,33,100],lst2:[9,0,81,-2,-56,],lst3:[12,31,87,1,0,4,-11]}\
                                  \nElija el diccionario:"))
                while submenu !=0:
                    
                        if submenu ==1:
                            diccionario1={"Raul":34,"Paula":19,"Jorge":43,"Richard":10,"Diana":3,"Isabel":76,"Gustavo":12,"Diego":37}
                            print(valores(diccionario1))
                            break
                        elif submenu ==2:
                        
                            diccionario2={"tplA":(4,-12,56,-34,98,102),"tplB":(9,0,1,10,-3,14),"tlpC":(87,12,56,987,-61)}
                            print(valores(diccionario2))
                            break
                        elif submenu ==3:
                            
                            diccionario3={"val1":-12.5,"val2":12.5,"val3":83,"val4":2.1,"val5":23,"val6":100,"val7":13.4,"val8":92}
                            print(valores(diccionario3))
                            break
                        elif submenu ==4:
                            
                            diccionario4={"lst1":[4,6,-12,56,-9,5.7,33,100],"lst2":[9,0,81,-2,-56,],"lst3":[12,31,87,1,0,4,-11]}
                            print(valores(diccionario4))
                            break
                        
                        else:
                            print("Elija una opción correcta en el submenú")
                        
                            submenu=int(input("Submenú: \n1 \n2 \n3 \n4 \nElija una opción del submenú:"))    
                                       
        elif menuprincipal == 2:
            print("Fin")
            break
        
        else:
            print("Seleccione la opción correcta")
        
        menuprincipal=int(input("Menú Principal: \n1: Demostración del cálculo de valores altos y bajos en diccionarios.\
                                \n2: Salir \nElija una opción:"))
