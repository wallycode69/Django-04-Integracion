# # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                 #
# Módulo 4 Integración - Ejercicios Integradores  #
#                                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Ejercicio 03: Escribir un programa que reciba una cadena de caracteres y 
#               devuelva un diccionario con cada palabra que contiene y la 
#               cantidad de veces que aparece (frecuencia).
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import time
print()

cadena = input("Ingrese una Cadena de Caracteres: ")
lista1 = cadena.lower().split(' ')
diccad = {}

def dic(lista):
    for i in lista:
        if not diccad.get(i):
            # print(i)         (Prueba de Escritorio)
            f = lista.count(i)
            # print(f)         (Prueba de Escritorio) 
            diccad[i] = f
    print(diccad)


# Programa Principal

print()
t0 = time.time()
dic(lista1)
t1 = time.time()
print(f"Tiempo de Proceso: {str(t1-t0)}")
print()

'''
Cadena de Caracteres para Probar la Función:

La Casa de la Colina ESTÁ EMBRUJADA pero como la casa está vendida ahora la que está embrujada es la colina

Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera

(Nota: No usar signos de puntuación: [comas, puntos, guiones, paréntesis, etc.])
'''



'''
# # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#   Tema: Encontrar Números Repetidos en Python
#  Autor: Manuel González (Oct-2020)
# Fuente: https://youtu.be/gZzTzM8vn6s
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # #

    for i in range(len(lista)):
        for j in range(len(lista)):
            if i != j:
                if lista[i] == lista[j] and lista[i] not in rep:
                    rep.append(lista[i])
'''

