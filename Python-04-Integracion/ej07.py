# # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                 #
# Módulo 4 Integración - Ejercicios Integradores  #
#                                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Ejercicio 07: Crear una clase llamada Cuenta que tendrá los siguientes 
#               atributos: titular (que es una persona) y cantidad (puede 
#               tener decimales). El titular será obligatorio y la cantidad es 
#               opcional. Crea los siguientes métodos para la clase:
#               - Un constructor, donde los datos pueden estar vacíos.
#               - Los setters y getters para cada uno de los atributos. El 
#                 atributo no se puede modificar directamente, sólo ingresando 
#                 o retirando dinero.
#               - mostrar(): Muestra los datos de la cuenta.
#               - ingresar(cantidad): Se ingresa una cantidad a la cuenta, si 
#                 la cantidad introducida es negativa, no se hará nada.
#               - retirar(cantidad): Se retira una cantidad de la cuenta. La 
#                 cuenta puede estar en números rojos.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

print()
import platform, os, time
from ej06 import Persona

class Cuenta(Persona):
# ------------------ Constructor de la Clase ------------------
	def __init__(self, titular = "", cantidad = 0):
		p = Persona()
		self.__titular  = p
		self.__cantidad = 0.0 #self.__validarCantidad()

# -------------------- Getters de Atributos --------------------
	@property
	def titular(self):
		return self.__titular

	@property
	def cantidad(self):
		return self.__cantidad

# -------------------- Setters de Atributos --------------------
#	@titular.setter
#	def titular(self):
#		self.__titular = self.Persona()

# ------------ Método: validarCantidad() + Setter --------------
	def __validarCantidad(self):
		salir = True
		while salir:
			try:
				cant = round(float(input(" Ingrese la Cantidad: ")), 2)
				if cant > 0:
					salir = False
					return cant
				else:
					print("Ingresó 0 (cero) o un Valor NEGATIVO, la Operación se Anula")
					input("Presione [ENTER] para Continuar...")
					cant = 0; salir = False
					return cant
			except ValueError:
				print("Debe Ingresar un VALOR ENTERO o DECIMAL (con (.) para separar la parte decimal)..!!!")
				print("-"*50)

	@cantidad.setter
	def cantidad(self):
		self.__cantidad = self.__validarCantidad()

# ------------------- Método: mostrarPesos() -------------------
	def mostrarPesos(self):
		cant = str(self.cantidad)
		cad  = ""; cont = 0; m3 = 0; cant2 = ""
		for i in range(len(cant)-1,-1,-1):
			if cant[i] == ".":
				cad += ","; cont += 1
			elif cont == 0:
				cad += cant[i]
			elif cont != 0 and cont == m3:
				if i - 1 == -1:
					cad += cant[i]; cont += 1; m3 += 3
				else:
					cad += cant[i] + "."; cont += 1; m3 += 3
			else:
				cad += cant[i]
				cont += 1
		for j in range(len(cad)-1,-1,-1):
			cant2 += cad[j]
		if cant2[-2] == ",":
			cant2 += "0"
		return cant2

# -------------------- Método: ingresar() ----------------------
	def __ingresar(self):
		print("Operación INGRESO/DEPÓSITO de Dinero en Efectivo:")
		print()
		cant1 = self.mostrarPesos()
		print(f'Su Saldo Anterior es: {cant1}')
		self.__cantidad += self.__validarCantidad()
		print()
		cant2 = self.mostrarPesos()
		print(f'Su Saldo Actual...es: {cant2}')
		input("Presione [ENTER] para Continuar...")
		opc = " "
		return opc

# -------------------- Método: retirar() -----------------------
	def __retirar(self):
		print("Operación EGRESO/RETIRO de Dinero en Efectivo:")
		print()
		cant1 = self.mostrarPesos()
		print(f'Su Saldo Anterior es: {cant1}')
		self.__cantidad -= self.__validarCantidad()
		print()
		cant2 = self.mostrarPesos()
		print(f'Su Saldo Actual...es: {cant2}')
		input("Presione [ENTER] para Continuar...")
		opc = " "
		return opc

# ---------------- Método: mostrar() + ToString ---------------
	def __str__(self):
		return 'Titular: {}, Saldo: {}'.format(self.titular.__str__(), self.cantidad)

	def mostrarDatos(self):
		cant = self.mostrarPesos()
		print('Titular de la Cuenta:')
		self.titular.mostrar()
		print(f'  Saldo: {cant}')
		input("Presione [ENTER] para Continuar...")
		opc = " "
		return opc

# -------------------- Método: salir() -------------------------
	def salir(self):
		self.limpiarPantalla()
		print("Gracias por Utilizar nuestro Sistema... Vuelva Pronto..!!!")
		print()
		opc = "0"
		return opc

# ---------------- Método: limpiarPantalla() -------------------
	def limpiarPantalla(self):
		if platform.system() == "Windows":
			os.system('cls')
		else:
			os.system('clear')

# --------------- Método: validarOpcionMenu() ------------------
	def __validarOpcionMenu(self):
		opciones = ["0", "1", "2", "3"]
		opc = input("Ingrese la Opción del Menú: ")
		while (opc == "" or opc not in opciones):
			print()
			print("Error de Ingreso:")
			print('a) Verifique que no haya presionado solo [ENTER].')
			print('b) Verifique que la Opción sea la Correcta.')
			print('c) Digite la Opción Requerida y Presione [ENTER].')
			print()
			self.limpiarPantalla()
			self.imprimirPantalla()
			opc = input("Ingrese la Opción del Menú: ")
		return opc

# --------------- Método: imprimirPantalla() -------------------
	def imprimirPantalla(self):
		self.limpiarPantalla()
		print(" "*14 + "# # # # # # # # # # # # # # # # # # # # # # # # # #")
		print(" "*14 + "#                                                 #")
		print(" "*14 + "#          BIENVENIDO A NUESTRO SISTEMA           #")
		print(" "*14 + "#          DE INGRESO / RETIRO DE DINERO          #")
		print(" "*14 + "#        (FUERTEMENTE VALIDADO..!!!  💪😜)        #")
		print(" "*14 + "#                                                 #")
		print(" "*14 + "#    MENÚ PRINCIPAL:                              #")
		print(" "*14 + "#                                                 #")
		print(" "*14 + "#    (1) - INGRESAR DINERO                        #")
		print(" "*14 + "#    (2) - RETIRAR  DINERO                        #")
		print(" "*14 + "#    (3) - MOSTRAR  DATOS DE LA CUENTA            #")
		print(" "*14 + "#                                                 #")
		print(" "*14 + "#    (0) - SALIR DEL SISTEMA                      #")
		print(" "*14 + "#                                                 #")
		print(" "*14 + "# # # # # # # # # # # # # # # # # # # # # # # # # #")
		print()

# --------------------- Método: menu() -------------------------
	def menu(self):
		opc = " "
		while opc != "0":
			self.limpiarPantalla()
			self.imprimirPantalla()
			opc = self.__validarOpcionMenu()
			match opc:
				case "0": opc = self.salir()
				case "1": opc = self.__ingresar()
				case "2": opc = self.__retirar()
				case "3": opc = self.mostrarDatos()

# --------------------- Método: menu() -------------------------
	def iniciar(self):
		self.menu()

# --------------------- Programa Principal ---------------------

c1 = Cuenta()

print()
c1.iniciar()
print()
