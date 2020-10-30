# tkinter
import os.path
from tkinter import *

class Programa:

    def __init__(self):
        self.title = "Master en Python"
        self.icon = ".img/logotipo.ico"
        self.icon_alt = "./21-tkinter/img/logotipo.ico"
        self.size = "750x400"
        self.resizable = False 

    def cargar(self):
        ventana = Tk()
        self.ventana = ventana


        ventana.title(self.title)

        ruta_icono = os.path.abspath(self.icon)

        texto = Label(ventana,text=ruta_icono)
        texto.pack()


        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icon_alt)

        # logotipo 
        #ventana.iconbitmap(ruta_icono)

        # tamaño
        ventana.geometry(self.size)


        # bloquea el tamaño
        if self.resizable:
            ventana.resizable(1, 1)
        else:
            ventana.resizable(1, 1)


    def mostrar(self):
        self.ventana.mainloop()


    def addTexto(self, texto="Hola"):
        self.texto = texto
        print(self.texto)
        texto = Label(self.ventana, text=self.texto)
        texto.pack()

# Instanciar mi programa

programa = Programa()
programa.cargar()
programa.addTexto("Hola Master Python")
programa.addTexto("Soy Willians")
programa.addTexto("Es interesante lo que he aprendido hasta ahora.!")
programa.mostrar()

