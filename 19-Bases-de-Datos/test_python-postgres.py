import psycopg2

def crear_BD():
    # crear las bd
    sql =  "SELECT  'CREATE DATABASE test_uno' "
    sql += "WHERE NOT EXISTS "
    sql += "(SELECT from pg_database WHERE datname = 'test_uno')"
    sql = "CREATE DATABASE test_uno;"
    print(sql)
    cursor.execute(sql)
    #cursor.execute('/\gexec')

def mirarBD():
    # mirar las BD
    cursor.execute("\l")
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

def show_tables():
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


#consultar()

def consultarPrecio():

    sql = "SELECT marca,precio from vehiculos WHERE precio  >= 15000 AND marca = 'Renault'"

    cursor.execute(sql)

    print("Coche con precios por encima de 15000 Marca Renault")
    for coche in cursor:
        print(coche)


#consultarPrecio()
 
def borrarRegistro():

    sql = "DELETE FROM vehiculos WHERE model = 'Saxo' "

    cursor.execute(sql)
    database.commit()

    if cursor.rowcount > 0:
        print(cursor.rowcount, "Eliminado")
    else:
        print("No hay cambios!")


#borrarRegistro()



def actualizar():

    sql = "UPDATE vehiculos SET model='Leon' WHERE marca='Seat' "

    cursor.execute(sql)

    database.commit()

    if cursor.rowcount > 0:
        print(cursor.rowcount, "Actualizado")
    else:
        print("No hay cambios!")

#actualizar()

try:
    # conexion
    connection = psycopg2.connect(user = "postgres",
    host="192.168.250.8",
    port="5400",
    password="hokusai8",
    database="postgres")

    cursor = connection.cursor()

    # Print PostgreSQL connection properties
    #print(connection.getr_dns_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

    crear_BD()

except (Exception, psycopg2.Error) as error:
    print("Error while connection to PostgreSQL", error)

finally:
    # Closing database connection
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL is closed")



