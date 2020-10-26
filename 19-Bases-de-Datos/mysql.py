import mariadb

# conexion
database = mariadb.connect(
    host="192.168.250.8",
    user="root",
    port=3064,
    passwd="9ayhDsBdyZ",
    database="master_python"
)

#print(database)

cursor = database.cursor()

def crearBD():
    # crear las bd
    sql = "CREATE DATABASE IF NOT EXISTS master_python"
    cursor.execute(sql)

def mirarBD():
    # mirar las BD
    cursor.execute("SHOW DATABASES")
    for bd in cursor:
        print(bd)

def crearTabla():
    # crear tablas
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vehiculos(
        id int(10) auto_increment not null,
        marca varchar(40) not null,
        model varchar(40) not null,
        precio float(10,2) not null,
        CONSTRAINT pk_vehiculo PRIMARY KEY(id)
    )
    """)

#crearTabla()

cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)


def insertarDatos():

    sql = "INSERT INTO vehiculos VALUES(null, 'Opel', 'Astra', 18500)"

    cursor.execute(sql)
    database.commit()

#insertarDatos()

def insertarVarios():
    
    coches = [
        ('Seat', 'Ibiza', 5000),
        ('Renault', 'Clio', 15000),
        ('Citroen', 'Saxo', 2000),
        ('Mercedes', 'Clase C', 35000)
    ]

    sql = "INSERT INTO vehiculos VALUES (null, %s, %s, %s)"

    cursor.executemany(sql, coches)
    database.commit()

#insertarVarios()


def consultar():

    sql = "SELECT * FROM vehiculos"

    cursor.execute(sql)
    result = cursor.fetchall()

    print("Todos los coches")
    for coche in result:
        print(coche[1], coche[3])


consultar()

def consultarPrecio():

    sql = "SELECT marca,precio from vehiculos WHERE precio  >= 15000 AND marca = 'Renault'"

    cursor.execute(sql)

    print("Coche con precios por encima de 15000 Marca Renault")
    for coche in cursor:
        print(coche)


consultarPrecio()
 
def borrarRegistro():

    sql = "DELETE FROM vehiculos WHERE model = 'Saxo' "

    cursor.execute(sql)
    database.commit()

    if cursor.rowcount > 0:
        print(cursor.rowcount, "Eliminado")
    else:
        print("No hay cambios!")


borrarRegistro()



def actualizar():

    sql = "UPDATE vehiculos SET model='Leon' WHERE marca='Seat' "

    cursor.execute(sql)

    database.commit()

    if cursor.rowcount > 0:
        print(cursor.rowcount, "Actualizado")
    else:
        print("No hay cambios!")

actualizar()


