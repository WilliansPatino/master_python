from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()

ventana.config(bd=70)

def mostrar_alerta():
	MessageBox.showwarning("Alerta", 
		"Disco casi lleno!")
	
def mostrar_error():
	MessageBox.showerror("Error", 
		"Campo invalido!")

def salir(nombre):
	
	resultado = MessageBox.askquestion("Salir", 
		"¿Continúa ejecutando la aplicación?")

	if resultado != "yes":

		MessageBox.showinfo("Salida", 
			f"Hasta luego {nombre}")

		ventana.destroy()



Button(ventana, text="Mostrar alerta", 
	command=mostrar_alerta).pack()


Button(ventana, text="Mostrar error", 
	command=mostrar_error).pack()


Button(ventana, text="Salir", 
	command=lambda: salir("Willians")).pack()


ventana.geometry("600x400")
ventana.title("Caja de dialogos en Tkinter")
ventana.config(
	bd=50,
	bg="#ccc"
	)


ventana.mainloop()
