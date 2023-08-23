# # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                 #
# Módulo 4 Integración - Ejercicios Integradores  #
#                                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Ejercicio 02: Escribir una función que calcule el mínimo común múltiplo entre
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

def mcm(a, b):
    c = math.lcm(a, b)
    return c


# Programa Principal

print()
print("* * * * * * * * * * * * * * * *")
print("* * *  Versión Reducida   * * *")
print("* * * * * * * * * * * * * * * *")
print()
t0 = time.time()
print(f"El Mínimo Común Múltiplo entre: {n1} y {n2} es: {str(mcm(n1, n2))}")
t1 = time.time()
print(f"Tiempo de Proceso: {str(t1-t0)}")
print()


# # # # # # # # # # # # # # # #
# # #  Versión Extendida  # # #
# # # # # # # # # # # # # # # #

print()

def mcd(x, y):
    z = math.gcd(x, y)
    return z

def minComMul(a, b):
    c = int((a * b) / mcd(a, b))
    return c


print("* * * * * * * * * * * * * * * *")
print("* * *  Versión Extendida  * * *")
print("* * * * * * * * * * * * * * * *")
print()
t2 = time.time()
print(f"El Mínimo Común Múltiplo entre: {n1} y {n2} es: {str(minComMul(n1, n2))}")
t3 = time.time()
print(f"Tiempo de Proceso: {str(t3-t2)}")
print()
