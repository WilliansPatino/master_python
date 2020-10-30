"""
	trabajar con text

"""

from tkinter import *

ventana = Tk()

ventana.geometry("500x500")

texto = Label(ventana, text="Bienvenido al programa")

def pruebas(nombre, apellidos, pais):
	return f"Hola {nombre} {apellidos} vive en {pais}"


texto.config(
	fg="white",
	bg="#000",
	padx=50,
	pady=20,
	font=("Arial", 14)
	)

texto.pack()

texto = Label(ventana, 
	text=pruebas(pais="Venezuela", 
		nombre="Willians", 
		apellidos="Patiño")
	)

texto.config(
	height=4,
	bg="orange",
	font=("Consolas",18),
	padx=10,
	pady=10,
	cursor="clock"
	) 

texto.pack(anchor=SE)



texto = Label(ventana, text="Master en Python")
texto.config(
	height=4,
	bg="green",
	font=("Consolas",12),
	padx=10,
	pady=10,
	cursor="clock"
	)

texto.pack(anchor=NW)




ventana.mainloop() 