'''
Montoya Montes Pedro 

LEER!: El programa usa codificación UNICODE para mostrar símbolos e 
imprimir más bonito, el programa está diseñado para que incluso si no soporta
dicha codificación de el resultado correctamente aunque en consola
se impriman mal algunas cosas.

V 1.2, el retorno del orden
-- Arreglado error en teorema ord_m(a)|phi(m), estaba cruzado en código.
V 1.3, raíz primitiva
-- Agregado calculo para saber si un número es raíz primitiva
--agregar phi(phi(m)) total de raices y calcular todas las raices
V 1.4, calculador raíces primitivas
-- Agregado para saber las raíces primitivas de un número m.
-- Modificado esquema de main y orden
V 1.4.1, modificado calculo de phi(n) y orden (ahora necesita pre calcular phi(m) como parámetro)
		debido a un bug (aún sin saber exactamente el origne) donde al calcular orden y raíces,
		phi(m) calculaba varias veces su valor.
V 1.5 Agregado calculo de índices y limpieza de código.

V 1.6 Agregado calculo de residuo cuadrático y mejora ligera en menú

Por agregar: calculo gcd, lcd
Cambiar idioma a inglés.
Cambiar/mejorar menú de selección
Cambiar doc
Agregar comentarios
agregar comprobación de residuo cuadrático (con a^(p-1/2) congr 1 mod m)
'''

from math import gcd #Importamos la biblioteca gcd directa de python 
import sys
'''
	Método que, dado un entero n, regresa su representación como superíndice.
	Entrada: un entero n.
	Salida: Una cadena con el entero n en su representación de superíndice.
'''
def superscript(n):
	return "".join(["⁰¹²³⁴⁵⁶⁷⁸⁹"[ord(c)-ord('0')] for c in str(n)]) 

'''
	Método que, dado un entero n, regresa su representación como subíndice.
	Entrada: un entero n.
	Salida: Una cadena con el entero n en su representación de subíndice.
'''
def subscript(n):
	return "".join(["₀₁₂₃₄₅₆₇₈₉"[ord(c)-ord('0')] for c in str(n)]) 

'''
	Método que, dado un entero n, regresa la función phi(n)
	Entrada: Un entero n a calcular su phi(n)
	Salida: Un entero que es el resultado de phi(n)
'''
def phi(n):
	cantidad = 0        
	i = 0
	while i < n:
		if gcd(n, i) == 1:
			cantidad += 1
			#print("cantidad=",cantidad, i)
		i = i +1
	return cantidad

'''
	Método que, dado un entero a y m, calcula el orden de a respecto del módulo m.
	Entrada: Un entero a y un entero m para calcular Ord_m(a)
	Salida: Un entero que es el resultado de Ord_m(a)
'''
def orden(a, m, phi_m):
	# Revisamos si efectivamente podemos hacer el algoritmo.
	if gcd(a,m) != 1:
		print("No se puede, (a,m) no son primos relativos", a,m)
		sys.exit()
	#Ahora ciclamos con las potencias.
	pot=1
	while pot<=phi_m: #Usamos el teorema de que Ord_m(a)<=phi(m)
		if (phi_m%pot) != 0 : #Usamos el teorema de que ord_m(a)|phi(m)
			pot=pot+1
		r=(a**pot)
		if r%m==1:	#Si el módulo de a^m=1, acabamos y encontramos solución (r).
			return (pot,r)
		pot=pot+1 

def indice(a,m,g):
	k=1 #Cambiar por multiplicacion para que sea menos operaciones
	while 1:
		if a == ((g**k)%m):
			return k
		k = k+1

def residuo_cuadratico(m):
	x = set([])
	for k in range(1,m):
		n=(k**2)%m
		print(k,superscript(2),"\u2261",n,"módulo",m)
		x.add(n)
	return x

def comprobar_residuo_euler(a,m):
	n=(m-1)/2
	if (a**n)%m == 1 :
		return True
	return False

def residuo_cuadratico_euler(m):
	x = set([])
	pot = (m-1)//2
	for k in range(1,m):
		if comprobar_residuo_euler(k,m):
			print(k,superscript(pot),"\u2261 1")
			x.add(k)
	print(x)		

'''
	El main.
'''

def main():
	print("Programa para calcular \u03D5(n) y Ord\u2098(a)\n")
	print("Lista de opciones:\n 1) Calcular \u03D5(n) \n 2) Calcular Ord\u2098(a)" )
	print(" 3) Comprobar ráiz primitiva\n 4) Calcular raíces primitivas") 
	print(" 5) Calcular indice\n 6) Calcular residuo cuadrático \n 7) Salir")

	operacion = input("Ingrese el número de la operación a realizar:")
	opcion =int(operacion)
	if opcion == 1:
		print("\n")
		valor_phi = input("Introduce el valor n: ")
		n = int(valor_phi)
		print(phi(n))
		return
	elif opcion == 2:
		print("\n")
		valor1 = input("Introduce el valor a: ")
		valor2 = input("Introduce el valor m: ")
		a = int(valor1)
		m = int(valor2)
		soluciones = orden(a,m) #Agregado para evitar hacer más calculos a futuro
		print("\u03D5(",m,")=",phi(m))
		orden1 = soluciones[0]
		r = soluciones[1]
		print(a,superscript(orden1),"=",r,"\u2261",r%m,"( mód",m,")")
		print("Ord",subscript(m),"(",a,")=",orden1)
		return
	elif opcion	== 3:
		print("\n")
		valor1 = input("Introduce el valor a: ")
		valor2 = input("Introduce el valor m: ")
		a = int(valor1)
		m = int(valor2)
		phi_m = phi(m)

		soluciones = orden(a,m,phi_m) #Agregado para evitar hacer más calculos a futuro
		orden1 = soluciones[0]
		r = soluciones[1]
		print("Ord",subscript(m),"(",a,")=",orden1)
		if phi_m==orden1:
			print("Sí es ráiz primitiva ya que  Ord",subscript(m),"(",a,")=","\u03D5(",phi_m,")")
			return
		print("No es ráiz primitiva")
		return
	elif opcion == 4:
		print("\n")
		valor = input("Introduce el valor m: ")
		m = int(valor)
		phi_m =phi(m)
		total_raices=phi(phi_m)
		print(m," tiene ",total_raices, "posibles raíces primitivas")
		print("\u03D5(",m,")=",phi_m)

		raices = []
		posible_raiz = 1
		while len(raices) < total_raices and posible_raiz < m: # and i < total_raices:
			while gcd(posible_raiz,m) != 1 and posible_raiz < m:
				posible_raiz = posible_raiz+1
			orden1 = orden(posible_raiz,m,phi_m)[0]
			if phi_m==orden1:
				print(posible_raiz, "es ráiz primitiva ya que Ord",subscript(m),"(",posible_raiz,")=","\u03D5(",m,") = ",phi_m)
				raices.append(posible_raiz)
			posible_raiz = posible_raiz +1

		if(len(raices) == 0):
			print(m, "no tiene raíces")
			return
		print("Las raíces de ",m, "son:")
		print(raices)
		return
	
	elif opcion == 5:
		print("\n")
		valor1 = input("Introduce el valor a: ")
		valor2 = input("Introduce el valor m: ")
		valor3 = input("Introduce el valor g: ")
		a = int(valor1)
		m = int(valor2)
		g = int(valor3)
		#Add full operation
		print("Ind",subscript(g),"(",a,") =",indice(a,m,g))
	elif opcion == 6:
		print("\n")
		valor = input("Introduce el valor m: ")
		m = int(valor)
		print(residuo_cuadratico(m))
	elif opcion == 7:
		return
	elif opcion == 8:
		return
	else:
		print("\n")
		print("Gracias por usar este programa uwu")
		return	

#main()

'''
indice(a,m,g):
indice(2,125,13)
'''

#residuo_cuadratico(13)
#residuo_cuadratico_euler(19)
#residuo_cuadratico_euler(37)
residuo_cuadratico_euler(101)



'''
print(comprobar_residuo_euler(10,11))
print(comprobar_residuo_euler(2,17))
print(comprobar_residuo_euler(11,29))
print(comprobar_residuo_euler(5,41))
'''