import os, shutil

# crear dire

mi_directorio = "./mi-carpeta"
if not os.path.isdir(mi_directorio):
    os.mkdir(mi_directorio)
else:
    print("ya existe el directorio")


# mostrar contenido del directorio

contenido = os.listdir(mi_directorio)
print(contenido)


for fichero in contenido:
    print(f"Fichero: {fichero}")

    