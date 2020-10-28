import usuarios.usuario as modelo
#                       alias
import notas.acciones


class Acciones:

    def registro(self):
        print("OK, vamoas a registrarte en el sistema...")

        nombre = input("Cual es tu nombre? ")
        apellidos = input("Cuales son sus apellidos? ")
        email = input("Introduce su email: ")
        password = input("Introduce  su contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)

        registro = usuario.registrar()

        if registro[0] >= 1:
            print("Se ha registrado con éxito")
            print(f"{registro[1].nombre} se ha registrado con el email {registro[1].email}")
        else:
            print("No te has registrado correctamente.!")

    def login(self):
        print("Bien!, Indique su login en el sistema")
        
        try:
            email = input("Introduce su email: ")
            password = input("Introduce su contraseña: ")

            usuario = modelo.Usuario('','', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"Bienvenido {login[1]}, te has registrado en el sistema el {login[5]}")
                self.proximasAcciones(login)


        except Exception as e:
            #print(type(e))
            #print(type(e).__name__)
            print(f"Login incorrecto! Intente mas tarde")

    
    def proximasAcciones(self, usuario):


        print("""
        Acciones disponibles:
         - Crear nota (crear)
         - Mostrar tus notas (mostrar)
         - Eliminar nota (eliminar)
         - Salir (salir)
        """)

        accion = input("¿Qué quiere hacer? ")
        
        haz = notas.acciones.Acciones()

        if accion == 'crear':
            print("Vamos a crear una nota")
            haz.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == 'mostrar':
            print("Vamos a mostrar una nota")
            haz.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == 'eliminar':
            print("Vamos a eliminar nota")
            haz.borrar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == 'salir':
            print(f"Hasta pronto, {usuario[1]}!")
            exit()



        pass
    
