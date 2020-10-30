
"""
	- Botones: radiocheck, check,
	- menu de opciones
"""


from tkinter import *
from tkinter import messagebox 

ventana = Tk()
ventana.title("Formularios con Tkinter")
ventana.config(
	bd=50,
	bg="#ccc"
	)
ventana.geometry("800x500")

encabezado = Label(ventana, text="Formularios 2")
encabezado.config(
	padx=15,
	pady=15,
	fg="white",
	font=("Consolas", 18),
	bg="green")

encabezado.grid(row=0, column=0, columnspan=6, sticky=W)

# botones check

def mostrar_profesion():
	texto = ""

	if web.get():
		texto += "Desarrollo Web"

	if movil.get():
		if web.get():
			texto += " y Desarrollo Movil"
		else:
			texto += "Desarrollo Movil"

	mostrar.config(text=texto,
		bg="blue",
		fg="white"
		)


web = IntVar()
movil = IntVar()


Label(ventana, 
	text="¿A qué te dedicas?",
	).grid(row=1, column=0)

Checkbutton(ventana,
	text="Desarrollo Web",
	variable=web,
	onvalue=1,
	offvalue=0,
	command=mostrar_profesion
	).grid(row=2, column=0)

Checkbutton(ventana,
	text="Desarrollo Movil",
	variable=movil,
	onvalue=1,
	offvalue=0,
	command=mostrar_profesion
	).grid(row=3, column=0)


mostrar = Label(ventana)
mostrar.grid(row=4, column=0)

# Radio buttons

def marcar():
	marcado.config(
		text=opcion.get(),
		bg="blue",
		fg="white"
		)


opcion = StringVar()
opcion.set(None)

Label(ventana, 
	text="¿Cual es tu género?").grid(row=5)
Radiobutton(ventana, 
	text="Masculino",
	variable=opcion,
	value="masculino",
	command=marcar
	).grid(row=6)
Radiobutton(ventana, 
	text="Femenino",
	variable=opcion,
	value="femenino",
	command=marcar
	).grid(row=7)

marcado = Label(ventana)
marcado.grid(row=8)


# option menu

def marcar_opcion():
	seleccionado.config(
		text=seleccion.get(),
		bg="blue",
		fg="white"
		)

seleccion = StringVar()
seleccion.set("Opcion 1")

Label(ventana, 
	text=" Elije una opción ").grid(row=5, column=1)
select = OptionMenu(ventana,
	seleccion,
	"Opcion 1",
	"Opcion 2",
	"Opcion 3"
	)
select.grid(row=6, column=1)

Button(ventana,
	text="Ver",
	command=marcar_opcion).grid(row=6, column=2)


seleccionado = Label(ventana)
seleccionado.grid(row=7, column=1)

ventana.mainloop()

