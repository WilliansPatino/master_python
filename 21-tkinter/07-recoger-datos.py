from tkinter import *

ventana = Tk()
ventana.geometry("600x400")
ventana.title("Entrada de datos en Tkinter")
ventana.config(
	bd=50,
	bg="#ccc"
	)

def get_dato():
	resultado.set(dato.get())

	if len(resultado.get()) >= 1:
		texto_recibido.config(
			bg="green",
			fg="white"
		)



dato = StringVar()
resultado = StringVar()

Label(ventana, 
	text="Introduce un texto").pack(anchor=NW)
Entry(ventana, textvariable=dato).pack(anchor=NW)

Label(ventana,
	text="Dato recibido: ").pack(anchor=NW)

texto_recibido = Label(ventana,
	textvariable=resultado)

# texto_recibido.config(
# 	bg="green",
# 	fg="white"
# 	)
texto_recibido.pack(anchor=NW)

Button(ventana, 
	text="Mostrar datos", command=get_dato).pack(anchor=NW)

ventana.mainloop()
