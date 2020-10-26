try:
    nombre = input("    ¿ Cual es su nombre?")

    if len(nombre) > 1:
        nombre += "Su nombre es:" + nombre

    print(nombre)
except:
    print("Debe ingresar su nombre")  
    pass
else:
    print("Entrada correcta de su nombre")
finally:
    print("Proceso de ingreso terminado!")