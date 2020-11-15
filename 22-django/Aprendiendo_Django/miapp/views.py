from django.shortcuts import render, HttpResponse, redirect
""" import mi modelos """
from miapp.models import Article

""" requerida para consultas ORM con OR """
from django.db.models import Q

""" Formularios con Clases """
from miapp.forms import formArticle

""" Sesiones/mensajes flash """
from django.contrib import messages

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

#-- Bloque:  crear articulos con ayuda de un formulario 

def save_article(request):
	# las variables se enviaran desde el formulario por la url
	
	try:
		# agregar el registro con GET
		# if request.method  == 'GET':
		if request.method  == 'POST':

			# title = request.GET['title']
			title = request.POST['title']

			if len(title) <=5:
				return HttpResponse("Tìtulo muy corto")

			""" content = request.GET['content']
			public = request.GET['public'] """
			content = request.POST['content']
			public = request.POST['public']

			articulo = Article(
				title = title,
				content = content,
				public = public
			)
			articulo.save()
			reg = f"<h2>Artículo agregado: {articulo.title} - {articulo.content} </h2>"
			return HttpResponse(reg)
	except:
		
		reg = f"<h2>No se pude agregar el articulo </h2>"
		return HttpResponse(reg)
	finally:
		# Redirige y mantiene actualizada cuando se hagan cambios
		return redirect('articulos')

def create_article(request):
	
	return render(request, 'create_article.html')

#--- Fin del bloque

#--Bloque: Formularios con Clases
def create_full_article(request):


		# validacion del formulario
	if request.method == 'POST':

		
			formulario = formArticle(request.POST)

			if formulario.is_valid():
				
				data_form = formulario.cleaned_data
				title = data_form.get('title')
				content = data_form['content']
				public = data_form['public']

				# salvar el registro
				articulo = Article(
					title = title,
					content = content,
					public = public
				)
				articulo.save()

				#  crear mensaje flash. mostrado solo una vez
				messages.success(request, f'Artículo registrado: {articulo.title}',
				)

				# redirigir al listado
				return redirect('articulos')

			else:

				#  crear mensaje flash. mostrado solo una vez
				messages.error(request, f'Error de entrada en el formulario')

				formulario = formArticle()
				return render(request, 'create_full_article.html',{'form':formulario}) 
	else:
				""" genera el formulario vacio """
				formulario = formArticle()

				return render(request, 'create_full_article.html',
				{
				'form': formulario
				}) 

	
#--FIn de bloque: Formularios....

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
	articulos = Article.objects.all()

	# Busqueda especifica por campos 
	articulos = Article.objects.filter(title__contains='blog')

	# exclusion // listar articulo que contenga 'blog' y sean privados.
	articulos = Article.objects.filter(title__contains='blog').exclude(
			public=False
		)
	
	# Consulta SQL pura
	sql = "SELECT * FROM miapp_article WHERE title LIKE '%blog%' "
	sql += "AND public=1"
	articulos = Article.objects.raw(sql)
	# Emplear  la consulta SQL pura reemplaza el ORM de Django

	# Otro clase de consulta del ORM de Django, utilizando el operando OR
	#  se requiere: from django.db.models import Q
	articulos = Article.objects.filter(
		Q(title__contains='blog') |
		Q(title__contains='Depp') |
		Q(public__contains=True)
	)

	# consulta final
	sql = "SELECT * FROM miapp_article WHERE public=1 ORDER BY id DESC; "
	# sql += "AND public=1"
	articulos = Article.objects.raw(sql)

	""" Algunas notas para lookup 
		puede agregar algo semejante a LIMIT

		1)Listar hasta 5 registros

			articulos = Article.objects.all()[:5]

		2) listar desde el record 3 hasta el 5

			articulos = Article.objects.all()[2:5]


		3) Sortear la salida:
			Article.objects.order_by('-id')
			Article.objects.order_by('title')

		4) Equivalente a LIKE  en SELECT ....

			articulos = Article.objects.filter(title__contains='STRING')

		5) Parecido a ILIKE  en SELECT ....

			articulos = Article.objects.filter(title__iexact='STRING')
		
		6) Buscar los ID a partir del 3ro.

			... = Article.objects.filter(id__gt=3)

		7) Buscar los mayores/igual a 3 o menores de 3.

			... = Article.objects.filter(id__gte=3)
			... = Article.objects.filter(id__lt=3)

		8) Buscar los mayores/igual a 3 y cuyo titulo contenga la palabra 'Articulo'

			... = Article.objects.filter(id__gte=3, title__contains='Articulo')

		9) listar los articulos ordenado descendente por id
		
			... =  Article.objects.all().order_by('-id')

	"""


	return render(request, 'articulos.html', {
		'articulos': articulos
	})

def borrar_articulo(request, id):

	articulo = Article.objects.get(pk=id)
	articulo.delete()

	#  crear mensaje flash. mostrado solo una vez
	messages.success(request, f'Artículo eliminado ID:{id}  {articulo.title}')
	# Redirige y mantiene actualizada cuando se hagan cambios
	return redirect('articulos')
