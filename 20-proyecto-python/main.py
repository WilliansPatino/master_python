"""
    Proyecto:

"""


from usuarios import acciones


print("""
        Opciones disponible en el menu
            - registro
            - login
""")

# instancia la clase
haz = acciones.Acciones()

accion = input("¿Qué desea hacer? ")

if accion == 'registro':
    haz.registro()

elif accion == 'login':
    haz.login() 

