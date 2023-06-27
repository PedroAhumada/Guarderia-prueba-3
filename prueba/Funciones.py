#FUNCIONES
import os
import time
import msvcrt
#import numpy as np Este es para los arreglos
#"arreglo1" = np.array([])0
#"arreglo2" = np.ones((1))
#"arreglo3" = np.zeros((1))
#"arreglo3" = np.zeros((1,6),int)

def validar_menu():
    while True:
        try:
            opcion=int(input("Ingrese un número: "))
            if opcion in (1,2,3,4):
                return opcion
        except:
            print("INGRESE UN NÚMERO VALIDO")
def validar_nombre():
      while True:
            nombre_usuario = input("Ingrese su nombre: ")
            if len(nombre_usuario.strip()) >= 3:
                return nombre_usuario
            else:
                print("ERROR! el nombre debe tener al menos 3 caracteres!")
def validar_rut():
        while True:
            try:
                rut = int(input("Ingrese rut(sin puntos ni dígito verificador): "))
                if len(str(rut))>=7 and len(str(rut))<=8:
                     return rut
                else:
                    print("ERROR! el rut debe tener entre 7 y 8 dígitos!")
            except:
                print("ERROR! debe ingresar un número entero!")

def validar_cantidad():
    while True:
        try:
            cantidad = int(input("Ingrese cantidad: "))
            if cantidad >= 0:
                return cantidad
            else:
                print("ERROR! CANTIDAD DEBE SER 0 O POSITIVA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
def validar_mascota():
      while True:
            nombre_usuario = input("Ingrese el nombre de su mascota: ")
            if len(nombre_usuario.strip()) >= 3:
                return nombre_usuario
            else:
                print("ERROR! el nombre debe tener al menos 3 caracteres!")
def validar_dia():
    while True:
        try:
            dia = int(input("Ingrese la cantidad de diás: "))
            if dia >= 1:
                return dia
            else:
                print("ERROR! CANTIDAD DEBE SER POSITIVA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")