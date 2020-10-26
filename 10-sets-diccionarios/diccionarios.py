"""
diccionarios

"""

# lista con diccionarios

contactos = [
	{
	'nombre': 'Willians',
	'email': 'wjospi@gmail.com'
	},
	{
	'nombre': 'Mine',
	'email': 'mine@gmail.com'
	},
	{
	'nombre': 'Cat',
	'email': 'crm@gmail.com'
	}	
]

print(contactos)

print(contactos[0]['nombre'])
print("\n",10*"*")
print("\nLista de contactos"+"\n"+20*"=")

for contacto in contactos:
	print(f"Nombre del contacto:  {contacto['nombre']}")
	print(f"Email del contacto:  {contacto['email']}")
	print(3*"-")