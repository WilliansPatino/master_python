from django.shortcuts import render, HttpResponse, redirect
""" import mi modelos """
from miapp.models import Article


# Create your views here.

#  MVC  = Modelo Vista Controlador
#  MVT  = Modelo Template Vista

layout = """
	 <h1>Sitio con Django | por Willians Patiño</h1>
    <hr>
    <ul>
        <li>
            <a href="/inicio">Inicio</a>
        </li>
        <li>
            <a href="/hola-mundo">Hola Mundo</a>
        </li>
        <li>
            <a href="/pagina">Página de Prueba</a>
        </li>
		  <li>
            <a href="/contacto">Contacto</a>
        </li>
		<li>
            <a href="/visitar_otra_pagina/">Redirigir a Página desde mi Web con parámetro opcional (ej: /1 o /4)</a>
        </li>
		<li>
            <a href="/visitar_google">Redirigir a Google desde mi Web</a>
        </li>
    </ul>
"""

def index(request):
	
	"""
	html = 
		<h2>Inicio</h2>
		<p>Años hasta el 2020</p>
		<ul>
	
		
	year = 2020
	while year <= 2050:
		
		if year % 2 == 0:
			html += f"<li>{str(year)}</li>"
			
		year += 1
		
	html += "</ul>"
	"""
	year = 2021
	rango = range(year, 2051)
	
	nombre = 'Willians Patiño'
	lenguajes = ['Perl', 'Bash','Python', 'JavaScript']
	#compilados = ['Java', 'Go', 'C++']
	compilados = []

	#return HttpResponse(layout+html)
	return render(request, 'index.html',
		{
			'title':'Título-inicio-dinámico',
			'mi_variable': 'Soy el contenido',
			'nombre':nombre,
			'lenguajes': lenguajes,
			'compilados': compilados,
			'years':rango
		}
	)

def visitar_otra_pagina(request, redirigir=0):

	if redirigir == 1:
		return redirect('/inicio/')

	elif redirigir == 4:
		# redirigir a contacto
		return redirect('contacto', nombre="Willians", apellido="Patiño")

	else:

		return HttpResponse(layout+"""
			<h2>Redirige Pagina de mi Web</h2>
			""")


def visitar_google(request):
	# return HttpResponse(layout+"""
	# 	<h2>Redirige a Google desde mi Web</h2>
	# 	""")
	return redirect('https://google.com')



def hola_mundo(request):
	# return HttpResponse(layout+"""
	# 	<h2>Hola Mundo, desde Django</h2>
	# 	<h3>Soy Willians, aprendiendo Python</h3>
	# 	""")
	return render(request, 'hola_mundo.html')
		
def pagina(request):
	# return HttpResponse(layout+"""
	# 	<h2>Pagina de mi Web</h2>
	# 	<h3>Creado por WP</h3>
	# 	""")
	return render(request, 'pagina.html',
		{'variable':'',
		'lista':['gatos','perros','caballos','aves','peces'],
		'citas':['Einstein','Gandhi','Mandela']
		}
	)
		
def contacto(request, nombre="", apellido=""):

	html = ""
	return render(request, 'contacto.html',
		{
			'nombre':nombre
		}
	 )

	if nombre or apellido:
		html = f"<em> {nombre} {apellido} </em>"

	# return HttpResponse(layout+
	# 	f"<h2>Contactar a</h2>"+html)


""" a partir de aqui para cntinuar con los modelos/tablas """

def crear_articulo(request, title='Sin indicar', content='Sin indicar', public=False):
	
	# crear el registro
	articulo = Article(
		title = title,
		content = content,
		public = public
	)

	articulo.save()

	reg = f"<h2>Articulo creado: {articulo.title} - {articulo.content} </h2>"
	return HttpResponse(reg)

def articulo(request, id='1'):

	try:
		articulo = Article.objects.get(id=id)

		""" otros ejemplos de busquedas 
			articulo = Article.objects.get(pk=5)
			articulo = Article.objects.get(title='Depp')
		"""
		reg = f"<h2>Articulo consultado: </h2> "
		reg += f"<strong>ID:  {articulo.id} <br/> "
		reg += f"<strong>Titulo:  {articulo.title} <br/> "
		reg += f"Contenido: {articulo.content} </strong>"
	except:
		reg = f"<h2>Articulo no encontrado </h2> "
	

	return HttpResponse(reg)

def actualizar_articulo(request, id):

		articulo = Article.objects.get(pk=id)

		articulo.title = 'Actualizado'
		articulo.content = ' contenido modificado'
		articulo.public = False

		articulo.save()

		reg = f"<h2>Articulo actualizado: </h2> "
		reg += f"<strong>ID:  {articulo.id} <br/> "
		reg += f"<strong>Titulo:  {articulo.title} <br/> "
		reg += f"Contenido: {articulo.content} </strong>"

		return HttpResponse(reg)

def articulos(request):

	# equivalente a un SELECT * FROM ...
	articulos = Article.objects.all()[2:5]
	
	""" puede agregar algo semejante a LIMIT

		1)Listar hasta 5 registros

			articulos = Article.objects.all()[:5]

		2) listar desde el record 3 hasta el 5

			articulos = Article.objects.all()[2:5]


	Sortear la salida:
		Article.objects.order_by('-id')
		Article.objects.order_by('title')

	"""


	return render(request, 'articulos.html', {
		'articulos': articulos
	})