# # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                 #
# Módulo 4 Integración - Ejercicios Integradores  #
#                                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Ejercicio 01: Escribir una función que calcule el máximo común divisor entre 
#               dos números.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # #
# # #  Versión Reducida   # # #
# # # # # # # # # # # # # # # #

import math, time
print()

n1 = int(input("Ingrese el 1er Número: "))
n2 = int(input("Ingrese el 2do Número: "))

def mcd(x, y):
    z = math.gcd(x, y)
    return z


# Programa Principal

print()
print("* * * * * * * * * * * * * * * *")
print("* * *  Versión Reducida   * * *")
print("* * * * * * * * * * * * * * * *")
print()
t0 = time.time()
print(f"El Máximo Común Divisor entre: {n1} y {n2} es: {str(mcd(n1, n2))}")
t1 = time.time()
print(f"Tiempo de Proceso: {str(t1-t0)}")
print()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # #  Versión Extendida (Algoritmo de Euclides Mejorado)   # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

print()

def maxComDiv(a, b):
    while a % b > 0:
        aux = a; a = b; b = aux % b
    return b

'''
     # # # # # # # # # # # # # # # # # # # # # # # # # # #
     # # #  Misma Función con Prueba de Escritorio   # # #
     # # # # # # # # # # # # # # # # # # # # # # # # # # #

print()

def maxComDiv(a, b):
    while a % b > 0:
        print("a%b =", a%b)
        aux = a;     print("aux <------ a =", aux)
        a = b;       print("  a <------ b =", a)
        b = aux % b; print("  b <-- aux%b =", b)
        print("--------------------")
    return b
'''


# Programa Principal

print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
print("* * *  Versión Extendida (Algoritmo de Euclides Mejorado)   * * *")
print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
print()
t2 = time.time()
print(f"El Máximo Común Divisor entre: {n1} y {n2} es: {str(maxComDiv(n1, n2))}")
t3 = time.time()
print(f"Tiempo de Proceso: {str(t3-t2)}")
print()
