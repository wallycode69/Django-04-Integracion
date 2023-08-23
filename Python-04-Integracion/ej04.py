# # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                 #
# Módulo 4 Integración - Ejercicios Integradores  #
#                                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Ejercicio 04: Escribir una función que reciba una cadena de caracteres y 
#               devuelva un diccionario con cada palabra que contiene y la 
#               cantidad de veces que aparece (frecuencia). Escribir otra 
#               función que reciba el diccionario generado con la función 
#               anterior y devuelva una tupla con la palabra más repetida y su 
#               frecuencia.
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

def tuplaMax(d):
    max_palabra = max(d.keys(), key=lambda k: d[k])
    max_frecuen = d[max_palabra]
    max_pal_fre = (max_palabra, max_frecuen)
    return max_pal_fre


# Programa Principal

print()
t0 = time.time()
dic(lista1)
tmax = tuplaMax(diccad)

print()
print(f"La Palabra Más Repetida es: {tmax[0]} ({tmax[1]})")

t1 = time.time()
print(f"Tiempo de Proceso: {str(t1-t0)}")
print()

'''
Cadena de Caracteres para Probar la Función:

La Casa de la Colina ESTÁ EMBRUJADA pero como la casa está vendida ahora la que está embrujada es la colina

Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera

(Nota1: No usar signos de puntuación: [comas, puntos, guiones, paréntesis, etc.])
(Nota2: La función tuplaMax() no contempla Máximos Repetidos)
'''


'''
# # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#   Tema: Máximo y Mínimo para un Diccionario en Python
#  Autor: John Ortiz Ordoñez (Oct-2019)
# Fuente: https://youtu.be/zep55auewKg
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # #

productos = {'Mouse': 29, 'Teclado': 57.9, 'Monitor': 299, 'Audífonos': 25.9}

print(productos)

prod_min = min(productos.keys(), key=lambda k: productos[k])
prod_max = max(productos.keys(), key=lambda k: productos[k])

print(prod_min, productos[prod_min])
print(prod_max, productos[prod_max])
'''