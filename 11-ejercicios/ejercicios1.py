"""
Ejercicio 1: un programa que tenga
una lista de 8 numeros y haga lo 
siguiente:
- Recorrer la lista y mostrarla
- Ordenarla y mostrarla
- mostrar su longitud
- buscar algun elemento (que el usuario
pida por teclado)
"""

# lista
numeros = [7,11,64,1948,27,1964]

# funciona que recorre cualquier 
# lista
def mostrarLista(lista):
	res = ""

	for elemento in lista:
		res += "Elemento: " + str(elemento) + "\n"

	return res

"""
# recorre y muestra la lista
for numero in 
"""

print(mostrarLista(numeros))

# ordenar y mostrar
print("*"*5 + " Ordenar/mostrar " + "*"*5 )

numeros.sort()
print(mostrarLista(numeros))

busqueda = int(input("Introduce el numero: "))

comprobar = isinstance(busqueda, int)

while not comprobar or busqueda <= 0:
	busqueda = int(input("Introduce el numero: "))
else:
	print(f"Has introducido el ¨{busqueda}")

	print("*** Buscar en la lista ***")

	searkch = numeros.index(busqueda)

	print(f"El numero buscado existe en la lista con el indice ¨{search}")k