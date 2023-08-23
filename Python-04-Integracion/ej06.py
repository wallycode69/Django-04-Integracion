# # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                 #
# Módulo 4 Integración - Ejercicios Integradores  #
#                                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Ejercicio 06: Crear una clase llamada Persona. Sus atributos son: nombre, 
#               edad, y DNI. Construya los siguientes métodos para la clase:
#               - Un constructor, donde los datos pueden estar vacíos.
#               - Los setters y getters para cada uno de los atributos. Hay que
#                 validar las entradas de datos.
#               - mostrar(): Muestra los datos de la persona.
#               - Es_mayor_de_edad(): Devuelve un valor lógico indicando si es 
#                 mayor de edad.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

print()

class Persona:
# ------------------ Constructor de la Clase ------------------
    def __init__(self, nombre = "", edad = 0, dni = ""):
        self.__nombre = self.__validarNombre()
        self.__edad   = self.__validarEdad()
        self.__dni    = self.__validarDNI()

# -------------------- Getters de Atributos --------------------
    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def dni(self):
        return self.__dni

# -------------- Método: validarNombre() + Setter --------------
    def __validarNombre(self):
        name = input("Ingrese el Nombre: ")
        while not name.isalpha() or len(name) < 2:
            print('Debe Ingresar un NOMBRE DE PERSONA (de no menos de 2 caracteres)..!!!')
            name = input("Ingrese el Nombre: ")
        nombre = name.capitalize()
        return nombre

    @nombre.setter
    def nombre(self):
        self.__nombre = __validarNombre()

# ---------------- Método: Es_mayor_de_edad() ------------------
    def Es_mayor_de_edad(self, e):
        return e >= 18

# ---------------- Método: validarEdad() + Setter --------------
    def __validarEdad(self):
        salir = True
        while salir:
            try:
                age = int(input("Ingrese la Edad: "))
                if self.Es_mayor_de_edad(age) and age <= 110:
                    salir = False
                    return age
                elif age < 1:
                    print("Debe Ingresar un VALOR ENTERO POSITIVO..!!!")
                elif age > 110:
                    print("Valor Fuera de Rango (Debe ser Menor a 110)..!!!")
                else:
                    print("NO ES MAYOR DE EDAD..!!!")
                    salir = False
                    return age
            except ValueError:
                print("Debe Ingresar un VALOR ENTERO POSITIVO..!!!")

    @edad.setter
    def edad(self):
        self.__edad = __validarEdad()

# ---------------- Método: validarDNI() + Setter ---------------
    def __validarDNI(self):
        doc = input("Ingrese el DNI: ")
        while (doc == "" or doc[0] == "0" or len(doc) < 7 or not doc.isdigit()):
            print()
            print("Error de Ingreso:")
            print('a) Verifique que no haya presionado solo [ENTER].')
            print('b) Verifique que el 1er Dígito NO SEA 0 (Cero).')
            print('c) Verifique que la Cantidad de Dígitos NO SEA MENOR a 7.')
            print('d) Se Ingresa todo junto: sin puntos, ni espacios, ni guiones.')
            print()
            doc = input("Ingrese el DNI: ")
        return doc

    @dni.setter
    def dni(self):
        self.__dni = __validarDNI()

# ---------------- Método: mostrar() + ToString ---------------
    def __str__(self):
        return 'Nombre: {}, Edad: {}, DNI: {}'.format(self.nombre, self.edad, self.dni)

    def mostrar(self):
        match len(self.dni):
            case 7: doc = (self.dni[0])   + "." + (self.dni[1:4]) + "." + (self.dni[4:])
            case 8: doc = (self.dni[0:2]) + "." + (self.dni[2:5]) + "." + (self.dni[5:])
            case 9: doc = (self.dni[0:3]) + "." + (self.dni[3:6]) + "." + (self.dni[6:])
        print(f' Nombre: {self.nombre}')
        print(f'   Edad: {self.edad} años')
        print(f'    DNI: {doc}')


# --------------------- Programa Principal ---------------------

#p1 = Persona()

#print()
#print(p1)
#print()
#p1.mostrar()
#print()

# ----------------------------- Fin -----------------------------







# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 
#              MÉTODOS DE VALIDACIÓN
# 
# validarNombre(): Valida las siguientes contingencias:
#                 - Si ingresaron directamente [Enter].
#                 - Si ingresaron caracteres alfanuméricos.
#                 - Si ingresaron sólo números.
#                 - Si ingresaron cualquier otro caracter 
#                   que no sea alfabético.
#                 - Si ingresaron menos de dos letras.
# 
# Nota: Sin importar cómo ingresan el dato (mayúsculas, 
#       minúsculas, o ambas) el método mostrar(), siempre
#       reporta el Nombre en minúscula con la inicial en
#       mayúscula.
# 
#   validarEdad(): Valida las siguientes contingencias:
#                 - Si ingresaron directamente [Enter].
#                 - Si ingresaron caracteres alfanuméricos.
#                 - Si ingresaron cualquier otro caracter 
#                   que no sea dígitos numéricos.
#                 - Si ingresaron números negativos o 
#                   0 (cero).
#                 - Si ingresaron valores fuera de rango 
#                   entre (1 - 110).
# 
# Nota: El método mostrar(), siempre acompaña al valor de
#       la edad con la palabra "años".
# 
#    validarDNI(): Valida las siguientes contingencias:
#                 - Si ingresaron directamente [Enter].
#                 - Si ingresaron caracteres alfanuméricos.
#                 - Si ingresaron cualquier otro caracter 
#                   que no sea dígitos numéricos.
#                 - Si ingresaron en el 1er dígito de la 
#                   izquierda un 0 (cero).
#                 - Si ingresaron menos de siete dígitos.
# 
# Nota: A pesar de que por la restricción del ingreso del 
#       DNI, el método mostrar(), siempre va a mostrar al
#       DNI con el formato XX.XXX.XXX con el punto (.), 
#       como separador de miles.
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #




'''
# # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#   Tema: CURSO de PYTHON 2020 ENCAPSULACIÓN
#  Autor: yacklyon (Nov-2019)
# Fuente: https://youtu.be/zzSIfxyEYBc
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Cliente:
    def __init__(self):
        self.__codigo = 4321

    def __cuenta(self):
        print('cuenta de procesamiento')

    def getcodigo(self):
        return self.__codigo

persona = Cliente()

print()
print(persona._Cliente__codigo)
persona._Cliente__cuenta()
'''