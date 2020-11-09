from django.shortcuts import render, HttpResponse, redirect

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
	
	html = """
		<h2>Inicio</h2>
		<p>Años hasta el 2020</p>
		<ul>
	"""
		
	year = 2020
	while year <= 2050:
		
		if year % 2 == 0:
			html += f"<li>{str(year)}</li>"
			
		year += 1
		
	html += "</ul>"
	
	#return HttpResponse(layout+html)
	return render(request, 'index.html' )

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
	return render(request, 'pagina.html')
		
def contacto(request, nombre="", apellido=""):

	html = ""

	if nombre or apellido:
		html = f"<em> {nombre} {apellido} </em>"

	return HttpResponse(layout+
		f"<h2>Contactar a</h2>"+html)