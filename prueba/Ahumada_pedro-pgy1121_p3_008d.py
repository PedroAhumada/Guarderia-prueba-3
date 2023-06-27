#Guarderia de perros
import os
import time
import msvcrt
import numpy as np
import Funciones as fun
lista_rut=[]
lista_dnombre=[]
lista_mnombre=[]
lista_dia=[]
lista_id=[]
id=0
id2=-1
guarderia=np.array([1,2,3,4,5,6,7,8,9,10],int)
print(guarderia)
while True:
    #os.system('cls')
    print("""MENÚ
        1.Registrar mascota
        2.Buscar mascota
        3.Retirar mascota y pagar
        4.Salir
        """) 
    print(lista_rut)
    opcion=fun.validar_menu()

    if opcion==1:
        print("Ustede eligio registrase")
        rut=fun.validar_rut()
        lista_rut.append(rut)
        dnombre=fun.validar_nombre()
        lista_dnombre.append(dnombre)
        #dar número único
        id=id+1
        lista_id.append(id)
        id2=id2+1
        mnombre=fun.validar_mascota()
        lista_mnombre.append(mnombre)
        dia=fun.validar_dia()
        lista_dia.append(dia)
        print("Registro completado con exíto")
        time.sleep(3)
        print("Seleccione una habitación")
        print(guarderia)
        habitacion=int(input("Escriba el número de la habitación deseada: "))
        if habitacion in (guarderia):
            print("habitación reservada")
            time.sleep(5)
    elif opcion==2:
        print("Ustede eligio Buscar mascota")
        rut=fun.validar_rut()
        if rut in lista_rut:
            pass
        else:
            print("El rut no se encuentra registrado")
    elif opcion==3:
        print("opcion 3")
        rut=fun.validar_rut()
        if rut in lista_rut:
            total=lista_dia()*15000
            print(f"SU TOTAL A PAGARE ES {total}")
        else:
            print("El rut no se encuentra registrado")
    else:
        print("Saliendo del programa.....")
        time.sleep(5)
        break
