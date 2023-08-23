# # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                 #
# Módulo 4 Integración - Ejercicios Integradores  #
#                                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Ejercicio 05: Sabiendo que ValueError es la excepción que se lanza cuando no 
#               podemos convertir una cadena de texto en su valor numérico, 
#               escriba una función get_int() que lea un valor entero del 
#               usuario y lo devuelva, iterando mientras el valor no sea 
#               correcto. Intente resolver el ejercicio tanto de manera 
#               iterativa como recursiva.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import time
print()

# # # # # # # # # # # # # # # #
# # #  Versión Iterativa  # # #
# # # # # # # # # # # # # # # #

def get_int_iterativa():
    valor = True
    while valor:
        try:
            entero = int(input("Ingrese un Valor Entero: "))
            print("PERFECTO..!!!  INGRESÓ UN VALOR CORRECTO..!!!")
            valor = False
        except TypeError:
            print("Valor Incorrecto..!!! (TypeError)  Debe ser un ENTERO..!!!")
        except ValueError:
            print("Valor Incorrecto..!!! (ValueError) Debe ser un ENTERO..!!!")
        except Exception:
            print("Valor Incorrecto..!!! (Exception)  Debe ser un ENTERO..!!!")
        else:
            print("FELICITACIONES..!!!  INGRESÓ UN VALOR ENTERO..!!!")
        finally:
            print("----------------------------------------------------------")

# # # # # # # # # # # # # # # #
# # #  Versión Recursiva  # # #
# # # # # # # # # # # # # # # #

def get_int_recursiva():
    try:
        entero = int(input("Ingrese un Valor Entero: "))
        print("PERFECTO..!!!  INGRESÓ UN VALOR CORRECTO..!!!")
    except ValueError:
        print("Valor Incorrecto..!!! (ValueError) Debe ser un ENTERO..!!!")
        get_int_recursiva()
    else:
        print("FELICITACIONES..!!!  INGRESÓ UN VALOR ENTERO..!!!")
    finally:
        print("----------------------------------------------------------")


# Programa Principal

print()
print("* * * * * * * * * * * * * * * *")
print("* * *  Versión Iterativa  * * *")
print("* * * * * * * * * * * * * * * *")
print()

print()
t0 = time.time()
get_int_iterativa()
t1 = time.time()
print(f"Tiempo de Proceso: {str(t1-t0)}")
print()


print()
print("* * * * * * * * * * * * * * * *")
print("* * *  Versión Recursiva  * * *")
print("* * * * * * * * * * * * * * * *")
print()

print()
t2 = time.time()
get_int_recursiva()
t3 = time.time()
print(f"Tiempo de Proceso: {str(t3-t2)}")
print()



'''
# # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#   Tema: Funciones Recursivas
#  Autor: Developer.pe (Abr-2020)
# Fuente: https://youtu.be/3D9_vkYe1Zo
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # #

def cuenta_atras(nro):
    nro -= 1
    if nro > 0:
        print(nro)
        cuenta_atras(nro)
    else:
        print("Terminamos de Contar..!!!")
    print(f"Orden de Liberación {nro}")

print()
cuenta_atras(10)

def factorial(nro):
    if nro > 1: nro *= factorial(nro - 1)
    return nro

print()
print(factorial(5))
'''