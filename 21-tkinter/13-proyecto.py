"""
Crear un programa que tenga:
	- Ventna
	- tamaño fijo
	- NO redimensionable
	- Un menu
	- Diferentes pantallas
	- Formularios de añadir productos
	- Guardar los datos temporalmente
	- Mostrar datos en un lista en la pantalla home
	- Opcion de salir
"""

from tkinter import *
from tkinter import ttk


# definir la ventana
ventana = Tk()

ventana.geometry("600x400")

# tamaño minimo de la ventana
#ventana.minsize("500x500")

ventana.title("Proyecto Tkinter - Master en Python")


# no se pueda cambiar de tamaño
ventana.resizable(0, 0)

# pantallas
def home():

		home_label.config(
			fg="gray",
			bg="lightblue",
			font=("Arial", 18),
			padx=190,
			pady=20
		)

		home_label.grid(row=0, column=0)

		products_box.grid(row=2)

		# Listar productos
		# for product in products:
		# 	if len(product) == 3:
		# 			product.append("added")
		# 			Label(products_box,
		# 				text=product[0]).grid()
		# 			Label(products_box,
		# 				text=product[1]).grid()
		# 			Label(products_box,
		# 				text=product[2]).grid()
		# 			Label(products_box,
		# 				text="---").grid()
		for product in products:
				if len(product) == 3:
						product.append("added")
						products_box.insert('',0,
							text=product[0],
							values = (product[1])
							)


		# ocultar otra pantallas
		add_label.grid_remove()
		info_label.grid_remove()
		data_label.grid_remove()
		add_frame.grid_remove()
		
		
		
	
		return True

def add():

		# Encabezado
		add_label.config(
			fg="gray",
			bg="lightblue",
			font=("Arial", 18),
			padx=80,
			pady=20
		)

		add_label.grid(row=0, column=0, 
			columnspan=10)

		# campos del formulario

		add_frame.grid(row=1)

		add_name_label.grid(row=1, column=0,
			padx=5, pady=5, sticky=E)
		add_name_entry.grid(row=1, column=1,
			padx=5, pady=5, sticky=W)

		add_price_label.grid(row=2, column=0,
			padx=5, pady=5, sticky=E)
		add_price_entry.grid(row=2, column=1,
			padx=5, pady=5, sticky=W)

		add_descr_label.grid(row=3, column=0,
			padx=5, pady=5, sticky=NW)
		add_descr_entry.grid(row=3, column=1,
			padx=5, pady=5, sticky=W)

		# estilo para la descripcion
		add_descr_entry.config(
			width=30,
			height=5,
			font=("Consolas",14),
			padx=14,
			pady=14
			)

		add_separator.grid(row=4, column=0)

		boton.grid(row=5, column=1, sticky=N)


		# ocultar otra pantallas
		home_label.grid_remove()
		info_label.grid_remove()
		data_label.grid_remove()
		products_box.grid_remove()

		
		

		return True

def info():

		info_label.config(
			fg="gray",
			bg="lightblue",
			font=("Arial", 18),
			padx=120,
			pady=20
		)

		info_label.grid(row=0, column=0)

		#data_label = Label(ventana, 
		#	text="Creado por Willians Patiño - 2020")
		
		data_label.grid(row=1, column=0)

		# ocultar otra pantallas
		home_label.grid_remove()
		add_label.grid_remove()
		add_frame.grid_remove()
		products_box.grid_remove()
		




		return True



# definicion campos de pantallas
home_label = Label(ventana, 
	text="Inicio")
add_label = Label(ventana, 
	text="Agregar productos")
info_label = Label(ventana, 
	text="Informaciòn")
data_label = Label(ventana, 
	text="Creado por Willians Patiño - 2020")


#products_box = Frame(ventana, width=250)

#TreeView
#Label(products_box).grid(row=0)
Label(ventana).grid(row=1)
products_box = ttk.Treeview(height=12, columns=2)
products_box.grid(row=1, column=0, columnspan=2)
products_box.heading("#0", text="Producto", anchor=W)
products_box.heading("#1", text="Precio", anchor=W)


def add_product():
		products.append([
			name_data.get(),
			price_data.get(),
			add_descr_entry.get("1.0", "end-1c")
			])

		name_data.set("")
		price_data.set("")
		add_descr_entry.delete("1.0", END)

		home()

# Variables
name_data = StringVar()
price_data = StringVar()
products = []


# campos del formulario

# frame
add_frame = Frame(ventana)

# nombre

add_name_label = Label(add_frame,
		text="Nombre del producto:")
add_name_entry = Entry(add_frame,
		textvariable=name_data)

# price
add_price_label = Label(add_frame,
		text="Precio:")
add_price_entry = Entry(add_frame,
		textvariable=price_data)

# descripcion
add_descr_label = Label(add_frame,
		text="Descripción:")
add_descr_entry = Text(add_frame)

# separador del boton
add_separator = Label(add_frame)	

# boton
boton = Button(add_frame, text="Guardar",
		command=add_product)

boton.config(
			bg="green",
			fg="white",
			pady=5,
			padx=15
			)



# cargar pantalla de inicio
home()


# Menu superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio",
		command=home)
menu_superior.add_command(label="Añadir",
		command=add)
menu_superior.add_command(label="Informacion",
		command=info)
menu_superior.add_command(label="Salir", 
		command=ventana.quit)


# cargar menu
ventana.config(menu=menu_superior)





ventana.mainloop()