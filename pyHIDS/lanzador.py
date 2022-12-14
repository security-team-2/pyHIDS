#!/usr/bin/env python3

import os
import random
import time

import conf

def salida():
    try:
        exit(0)
    except:
        print("Saliendo...")

if __name__ == '__main__':
    print("Bienvenido al entorno de configuración de HIDS INSEGUS")

    #Comprobamos si el fichero donde almacenamos la base de datos existe mediante su path
    if not os.path.exists(conf.BASE_PATH):
        print("Aún no ha sido generada la base de datos de seguridad...")
        gen_base = input("Generar base de datos [y/n]: ")
        if gen_base=="y":
            exec(open(os.path.join(conf.PATH,"genBD.py")).read())
            sistemaop = os.name
            #Windows
            if sistemaop=="nt":
                #Establecemos que nos haga un resumen mensual del conjunto de incidencias en la base de datos
                os.system(conf.TASKRESUMW)
            #Linux
            else:
                #Establecemos que nos haga un resumen mensual del conjunto de incidencias en la base de datos
                os.system(conf.TASKRESUML)

        
        print("\nOpción 1: Establecer periodo de revisión")
        print("Opción 2: Salir de entorno de configuración")
        case = int(input("Escoja opción: "))
    
        while case >2 or case==0:
            case = int(input("Debe escoger entre [1 | 2 | 3], escoja opción: "))
        if case==1:
            print("Se realizan revisiones diarias")
            horaDia = input("Establecer hora de revisión: ")
            sistemaop = os.name
            #Windows
            if sistemaop=="nt":
                os.system(conf.TASKSC+horaDia)
            #Linux
            else:
                os.system(conf.TASKCR)
            salida()
        else:
            salida()
            
    #Si la base de hash no existe no tiene sentido realizar una revisión
    else:

        print("\nOpción 1: Establecer periodo de revisión")
        print("Opción 2: Realizar revisión")
        print("Opción 3: Salir de entorno de configuración")

        case = int(input("Escoja opción: "))

        while case >3 or case==0:
            case = int(input("Debe escoger entre [1 | 2 | 3], escoja opción: "))
            
        if case==1:
            print("Se realizan revisiones diarias")
            horaDia = input("Establecer hora de revisión: ")
            sistemaop = os.name
            #Windows
            if sistemaop=="nt":
                os.system(conf.TASKSC+horaDia)
            #Linux
            else:
                os.system(conf.TASKCR)
            salida()
        elif case==2:
            print("Realizando revisión...")

            try:
                inicio= time.time()
                exec(open(os.path.join(conf.PATH,"pyHIDS.py")).read())

            except Exception as e:
                print(e)
            
            print(""+"\nRevisión finalizada")
            fin = time.time()
            print("tiempo de ejecucion: ",fin-inicio,"segundos")
            case2 = input("¿Desea actualizar la base de datos existente? [y/n]: ")

            if case2 == "y":

                case3 = input("Si algún fichero ha sufrido una modificación de su integridad podrían estar en peligro"+ \
                                    "\nla información almacenada en ellos, ¿está seguro de actualizar la base de datos? [y/n]: ")                  
                if case3=="y":
                    x = random.random()
                    
                    #Solo se ejecutará el 30% de las veces que se desee modificar la base de hash
                    if x<0.3:
                        #Iniciamos el Hand-Shake Protocol
                        exec(open(os.path.join(conf.PATH,"randomChallenge.py")).read())
                    else:  
                        exec(open(os.path.join(conf.PATH,"genBD.py")).read())
                else:
                    salida()
            else:
                salida()
        elif case==3:
            salida()