"""
	Calculadora
	- dos campos de texto
	- 4 boitnoes de operaciones
	- mostrar el resultado

"""
from tkinter import *
from tkinter import messagebox 

ventana = Tk()
ventana.title("Ejercicio completo con Tkinter")
ventana.config(
	bd=50,
	bg="#ccc"
	)
ventana.geometry("500x400")

def sumar():
	try:
		resultado.set(float(numero1.get()) +
			float(numero2.get())
			)
		mostrar_resultado()
	except:
		mostrar_error()

def restar():
	try:
		resultado.set(float(numero1.get()) -
			float(numero2.get())
			)
		mostrar_resultado()
	except:
		mostrar_error()


def multiplicar():
	try:
		resultado.set(float(numero1.get()) *
			float(numero2.get())
			)
		mostrar_resultado()
	except:
		mostrar_error()


def dividir():
	try:
		resultado.set(float(numero1.get()) /
			float(numero2.get())
			)
		mostrar_resultado()
	except:
		mostrar_error()



def mostrar_resultado():
	messagebox.showinfo("Resultado",
		f"\nEl Resultado de la operación es:\n\r\t {resultado.get()}")



def mostrar_alerta():
	messagebox.showwarning("Alerta", 
		"Disco casi lleno!")
	
def mostrar_error():
	messagebox.showerror("Error", 
		"Campo invalido!")

def salir(nombre):
	
	resultado = messagebox.askquestion("Salir", 
		"¿Continúa ejecutando la aplicación?")

	if resultado != "yes":

		messagebox.showinfo("Salida", 
			f"Hasta luego {nombre}")

		ventana.destroy()


numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

marco = Frame(ventana, width=310, height=200)
marco.config(
	bd=1,
	relief=SOLID,
	padx=15,
	pady=15
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

Label(marco, text="primer numero: ").pack()
Entry(marco, textvariable=numero1, justify="center").pack()

Label(marco, text="segundo numero: ").pack()
Entry(marco, textvariable=numero2, justify="center").pack()

Label(marco, text="").pack()

Button(marco, text="Sumar",
	command=sumar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Restar",
	command=restar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Multiplicar",
	command=multiplicar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Dividir",
	command=dividir).pack(side="left", fill=X, expand=YES)

# macros



# Button(ventana, text="Mostrar alerta", 
# 	command=mostrar_alerta).pack()


# Button(ventana, text="Mostrar error", 
# 	command=mostrar_error).pack()


# Button(ventana, text="Salir", 
# 	command=lambda: salir("Willians")).pack()




ventana.mainloop()
