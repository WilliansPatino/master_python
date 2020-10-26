""" 

Ejercicio 3: Programa que compruebe si
una variable esta vacia. Si esta vacia rellenarla 
con texo en minusculas y mostrarla en mayusculas.
"""

variable = ""

if len(variable.strip()) <= 0:
	variable = "ahora tiene contenido"
	print(variable)
else:
	print(f"La variable no tiene contenido {variable}")
	print(len(variable))


print("-- ahora en mayusculas --")
print(variable.upper())
