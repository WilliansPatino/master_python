"""
	trabajar con text

"""

from tkinter import *

ventana = Tk()

ventana.geometry("700x700")
ventana.title("Marcos en Tkinter | Master en Python")
texto = Label(ventana, text="Bienvenido al programa")

# marco padre
marco_padre = Frame(ventana, width=250, height=250)
marco_padre.config(bg="lightgreen",
	bd=5,
	relief="solid")
marco_padre.pack(side=BOTTOM, fill=X, expand=YES)


marco = Frame(marco_padre, width=250, height=250)
marco.config(bg="red",
	bd=5,
	relief="raised")

marco.pack(side=LEFT, anchor=SW)
marco.pack_propagate(False)

#texto = Label(marco, text="Primer marco").pack(side=BOTTOM, anchor=CENTER)
texto = Label(marco, text="Primer marco")
texto.config(
	bg="red",
	fg="white",
	font=("Arial",14),
	height=25,
	width=15,
	anchor=CENTER
	)
texto.pack()

marco = Frame(marco_padre, width=250, height=250)
marco.config(bg="lightblue",
	bd=5,
	relief="raised")
marco.pack(side=RIGHT, anchor=SE)

marco_padre = Frame(ventana, width=250, height=250)
marco_padre.config(bg="lightblue",
	bd=5,
	relief="raised")
marco_padre.pack(side=TOP, anchor=N, fill=X, expand=YES)


ventana.mainloop()
