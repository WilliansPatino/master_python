from tkinter import *

ventana = Tk()
ventana.geometry("700x400")
ventana.title("Formularios en Tkinter")

# text encabezado
encabezado = Label(ventana, text="Formulario con Tkinter")
encabezado.config(
	fg="white",
	bg="darkgray",
	font=("Open Sans",18),
	padx=10,
	pady=10
	)

# encabezado.pack(side=LEFT, anchor=NW)
# NOTA:  al utilizar grid, se tiene que sustituir el pack
# - ejemplo de uso # 1
#encabezado.grid(row=0, column=0, columnspan=6, sticky=W)
# - ejemplo de uso # 2
encabezado.grid(row=0, column=0)




# label para el campo: NOMBRE
label = Label(ventana, text="Nombre")
label.grid(row=1, column=0, sticky=W,
	padx=5, pady=5)
# campo de texto
campo_text = Entry(ventana)
campo_text.grid(row=1, column=1, 
	padx=5, pady=5)
campo_text.config(justify="right", state="normal")

# label para el campo: APELLIDO
label = Label(ventana, text="Apellido")
label.grid(row=2, column=0, sticky=W, 
	padx=5, pady=5)
# campo de texto
campo_texto = Entry(ventana)
campo_texto.grid(row=2, column=1, 
	padx=5, pady=5)
campo_texto.config(justify="right", state="normal")
#campo_texto.config(justify="right", state="disable")

# descripcion
label = Label(ventana, text="Descripcion")
label.grid(row=3, column=0, sticky=W,
	padx=5, pady=5)
# campo de texto grande
campo_grande = Text(ventana)
campo_grande.grid(row=3, column=1)
campo_grande.config(
	width="30",
	height=5,
	font=("Arial",12),
	padx=15,
	pady=15
	)



# Botones
Label(ventana).grid(row=4, column=1)

boton = Button(ventana, text="Enviar")
boton.grid(row=5, column=1, sticky=W)
boton.config(
	padx=15,
	pady=15,
	bg="gray",
	fg="white"
	)


ventana.mainloop()
