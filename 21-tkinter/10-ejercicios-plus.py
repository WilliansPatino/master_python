"""
	Calculadora
	- dos campos de texto
	- 4 botones de operaciones
	- mostrar el resultado

	crear clase y objetos

"""
from tkinter import *
from tkinter import messagebox 



class Calculadora:

	

	def __init__(self, alertas):
		self.numero1 = StringVar()
		self.numero2 = StringVar()
		self.resultado = StringVar()
		self.alertas = alertas


	def sumar(self):
		try:
			self.resultado.set(float(self.numero1.get()) +
				float(self.numero2.get())
				)
			self.mostrar_resultado()
		except:
			self.mostrar_error()

	def restar(self):
		try:
			self.resultado.set(float(self.numero1.get()) -
				float(self.numero2.get())
				)
			self.mostrar_resultado()
		except:
			self.mostrar_error()


	def multiplicar(self):
		try:
			self.resultado.set(float(self.numero1.get()) *
				float(self.numero2.get())
				)
			self.mostrar_resultado()
		except:
			self.mostrar_error()


	def dividir(self):
		try:
			self.resultado.set(float(self.numero1.get()) /
				float(self.numero2.get())
				)
			self.mostrar_resultado()
		except:
			self.mostrar_error()


	def mostrar_resultado(self):
		self.alertas.showinfo("Resultado",
			f"\nEl Resultado de la operación es:\n\r\t {self.resultado.get()}")


	def mostrar_alerta(self):		messagebox.showwarning("Alerta", 
			"Disco casi lleno!")
		
	def mostrar_error(self):
		messagebox.showerror("Error", 
			"Campo invalido!")



def salir(nombre):
	
	resultado = messagebox.askquestion("Salir", 
		"¿Continúa ejecutando la aplicación?")

	if resultado != "yes":

		messagebox.showinfo("Salida", 
			f"Hasta luego {nombre}")

		ventana.destroy()


ventana = Tk()
ventana.title("Ejercicio completo con Tkinter")
ventana.config(
	bd=50,
	bg="#ccc"
	)
ventana.geometry("500x400")

calculadora = Calculadora(messagebox)




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
Entry(marco, textvariable=calculadora.numero1, justify="center").pack()

Label(marco, text="segundo numero: ").pack()
Entry(marco, textvariable=calculadora.numero2, justify="center").pack()

Label(marco, text="").pack()

Button(marco, text="Sumar",
	command=calculadora.sumar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Restar",
	command=calculadora.restar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Multiplicar",
	command=calculadora.multiplicar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Dividir",
	command=calculadora.dividir).pack(side="left", fill=X, expand=YES)

# macros



# Button(ventana, text="Mostrar alerta", 
# 	command=mostrar_alerta).pack()


# Button(ventana, text="Mostrar error", 
# 	command=mostrar_error).pack()


# Button(ventana, text="Salir", 
# 	command=lambda: salir("Willians")).pack()




ventana.mainloop()
