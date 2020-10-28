import notas.nota as modelo

class Acciones:


    def crear(self, usuario):
        print(f"\n {usuario[1]} vamos a crear una nota ")
       
        titulo = input("Introduce el título de la nota: ")
        descripcion = input("Introduce el contenido de la nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f" Perfecto!!  la nota se ha guardado {nota.titulo}")
        else:
            print(f" \n no se guardado la nota {usuario[1]}")


    def mostrar(self, usuario):
        print(f" OK {usuario[1]} aqui tiene tus notas ")

 
        nota = modelo.Nota(usuario[0])
        notas = nota.listar()
        #print(notas)
        for nota in notas:
            print("\n***")
            print(nota[2])
            print(nota[3])
            print("\n***")

    def borrar(self, usuario):
        print(f"De acuerdo {usuario[1]} se va a eliminar una nota")

        titulo = input("Introduce el titulo de la nota: ")

        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f" Se ha eliminado la nota {nota.titulo}")
        else:
            print("No se ha eliminado la nota")



