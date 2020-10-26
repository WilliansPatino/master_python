# importa todas las fnciones
import mimodulo

# importa solamente la funcion deseada
from mimodulo import bienvenida

# importa todas
# from mimodulo import *

#print(mimodulo.bienvenida("Willians"))

print(bienvenida("Mine"))

import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()

print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.day)
fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")

print(f"fecha personalizada: {fecha_personalizada}")

# 66. modulo matematicas
