"""

Ejercicio 2. Escribir un programa que
añada valores a una lista
mientras que su longitud sea menor
a 120 y luego mostrar la lista.
"""

lista = []
longitud = 0

while longitud < 120:

	for elemento in range(0, 121):
		lista.append(elemento)

		longitud = len(lista)

print("-- Lista ---")
for elemento in lista:
	print(f"Elemento: {elemento}")

print(lista)

print("--- resultado segun el curso ---")
