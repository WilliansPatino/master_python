from flask import Flask, redirect, url_for, render_template, request
from datetime import datetime
from flask_mysqldb import MySQL
from flask import flash


app = Flask(__name__)

# necesario CLAVE SECRETA
app.secret_key = 'pr0j3ctflask'

# conexión con la base de datos
app.config['MYSQL_HOST'] = '192.168.250.9'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'masterpython'
app.config['MYSQL_DB'] = 'proyectoflask'

mysql = MySQL(app)


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

@app.route('/agregar-coche', methods=['GET', 'POST'])
def agregar_coche():

    if request.method == 'POST':

        marca = request.form['marca']
        modelo = request.form['modelo']
        precio = request.form['precio']
        ciudad = request.form['ciudad']
   
        
        cur = mysql.connection.cursor()
        #cur.execute("INSERT INTO coches VALUES(NULL,'Fiat','Sienna',3500,'Caracas',null)")

        # Right syntax  to use at SQL 
        sql = """INSERT INTO coches VALUES(null,%s, %s, %s, %s)"""
        cur.execute(sql, (marca, modelo, precio, ciudad))
        cur.connection.commit()
        cur.close()
        flash('Registrado con éxito')

        
    
        return redirect(url_for('index'))
        

    return render_template('crear_coche.html')

@app.route('/coches')
def coches():
    cur = mysql.connection.cursor()
    sql = "SELECT * from coches ORDER BY id DESC;"
    cur.execute(sql)
    
    coches = cur.fetchall()
    cur.close()

    return render_template('coches.html', coches=coches)


@app.route('/coche/<coche_id>')
def coche(coche_id):
    cur = mysql.connection.cursor()
    sql = """SELECT * from coches WHERE id = %s"""
    cur.execute(sql, (coche_id))
    
    coche = cur.fetchone()
    cur.close()

    return render_template('coche.html', coche=coche)

@app.route('/borrar_coche/<coche_id>')
def borrar_coche(coche_id):
    cur =  mysql.connection.cursor()
    sql = f"DELETE from coches WHERE id = {coche_id};"
    cur.execute(sql)
    mysql.connection.commit()
    
    flash('Registrado ha sido eliminado')
   

    return redirect(url_for('coches'))


@app.route('/editar_coche/<coche_id>', methods=['GET', 'POST'])
def editar_coche(coche_id):

    if request.method == 'POST':

        marca = request.form['marca']
        modelo = request.form['modelo']
        precio = request.form['precio']
        ciudad = request.form['ciudad']
   

        cur =  mysql.connection.cursor()
        sql = """
                UPDATE coches 
                SET marca = %s,
                    modelo = %s,
                    precio = %s,
                    ciudad = %s
                WHERE id = %s
            """
        
        cur.execute(sql, (marca, modelo, precio, ciudad, coche_id))
        cur.connection.commit()
        cur.connection.close()
    
        flash('Registrado ha sido actualizado con éxito!')
   
        return redirect(url_for('coches'))
  

    cursor = mysql.connection.cursor()
    sql = """SELECT * from coches WHERE id = %s"""
    cursor.execute(sql, (coche_id))
    coche = cursor.fetchall()
    cursor.close()
    
    return render_template('crear_coche.html', coche=coche[0])


if __name__ == '__main__':
    app.run(debug=True)

    
"""  Como se recibe/captura los datos desde el POST

    marca = request.form['marca']
    modelo = request.form['modelo']
    precio = request.form['precio']
    ciudad = request.form['ciudad']
    return f" {marca} {modelo} {precio} {ciudad}"


"""