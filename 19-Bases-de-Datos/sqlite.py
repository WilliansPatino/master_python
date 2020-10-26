import sqlite3

# crear la BD
conexion = sqlite3.connect("prueba.db")

cursor = conexion.cursor()

# crear tabla
"""
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+ 
    "id INTEGER PRIMARY KEY AUTOINCREMENT,"+
    "titulo varchar(255),"+
    "description text,"+
    "precio int(255)"+
    ")"
)
"""

cursor.execute("""
CREATE TABLE IF NOT EXISTS productos( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo varchar(255),
    description text,
    precio int(255)
);
""")




# guardar cambios
conexion.commit()

# insertar datos en la table
cursor.execute("INSERT INTO productos VALUES (null, 'Cuaderno','Descripcion del producto',500)")


# borrar todos
cursor.execute("DELETE from productos;")
conexion.commit()

# insertar varios registros de una vez
productos = [
    ('Pantalla de 32 HD',' Monitor Gama media',140),
    ('Pantalon Levis Azul','Jean Levis 505', 65),
    ('Calzado Sport',' zapatos NIke Gama media',40),
    ('Franela','Franela puro algodon',20),
]
cursor.executemany("INSERT INTO productos VALUES (null, ?,?,?)", productos)
conexion.commit()

# listar los registros
cursor.execute("SELECT * FROM productos;")
productos = cursor.fetchall()
print(productos)



# for producto in productos:
#     print("ID: ", producto[0])
#     print("Titulo: ", producto[1])
#     print("Descripcion: ", producto[2])
#     print("Costo: ", producto[3])
#     print(5*"-")


# listar producto segun una busqueda
cursor.execute("SELECT * FROM productos WHERE precio >=100;")
productos = cursor.fetchall()

for producto in productos:
    print("ID: ", producto[0])
    print("Titulo: ", producto[1])
    print("Descripcion: ", producto[2])
    print("Costo: ", producto[3])
    print(5*"-")



cursor.execute("""
SELECT titulo FROM productos;
""")
producto = cursor.fetchone()
print(producto)

# update / actualizar productos
cursor.execute("UPDATE productos SET precio=150.99 WHERE precio = 140")
conexion.commit()

# cierra la BD
conexion.close()