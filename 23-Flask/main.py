from flask import Flask, redirect, url_for, render_template
from datetime import datetime

app = Flask(__name__)

# context processors: codigo disponible en cualquier pagina

@app.context_processor
def date_now():
    return {
        'fecha': datetime.utcnow()
    }


# endpoints

# rutas
@app.route('/')
def index():
    
    edad = 56
    personas =['Vitor', 'Willians','Minerva' ]


    return render_template('index.html',
        title="Aprendiendo Flask",
        dato1 = 'Valor 1',
        dato2 = 'Valor 2',
        lista = ['uno', 'dos','tres' ],
        edad = edad,
        personas = personas

    )

# otra ruta, con pase de argumentos
@app.route('/informacion/<nombre>/<apellidos>')
def informacion(nombre, apellidos):
    
    return render_template('informacion.html',
        title = 'Información del cliente',
        nombre=nombre,
        apellidos=apellidos
    )


# otra ruta, con pase de argumentos opcionales
@app.route('/contacto')
@app.route('/contacto/<string:nombre>')
def contacto(nombre = None):

    texto = ""
    nombre=""
    if nombre != None:
            texto = f"<H2> {nombre} </h2>"
            
    
    return render_template('contacto.html',
        title = 'Contacto',
        texto=texto
    )
    

# una ruta con redireccion a otra pagina
@app.route('/otra-pagina')
@app.route('/otra-pagina/<redireccion>')
def otra_pagina(redireccion = None):

    if redireccion is not None:
        return redirect(url_for('lenguajes'))

    return "<h2> Pagina de redireccion </h2>"



@app.route('/lenguajes')
def lenguajes():

    texto = 'Aprendiendo Python,CSS y JavaScript'

    return render_template('lenguajes.html')

"""   return f
        <h1>Otra página:</h1>
        <HR/>
        {texto}

"""


if __name__ == '__main__':
    app.run(debug=True)

    