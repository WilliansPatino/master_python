from django.shortcuts import render, HttpResponse

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
	
	return HttpResponse(layout+html)

def hola_mundo(request):
	return HttpResponse(layout+"""
		<h2>Hola Mundo, desde Django</h2>
		<h3>Soy Willians, aprendiendo Python</h3>
		""")
		
def pagina(request):
	return HttpResponse(layout+"""
		<h2>Pagina de mi Web</h2>
		<h3>Creado por WP</h3>
		""")
