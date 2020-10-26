import sqlite3

dbfile = 'usuarios.db'
conexion = sqlite3.connect(dbfile)

cursor = conexion.cursor()

# crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email varchar(255),
    username varchar(255),
    password varchar(255)
);
""")

conexion.commit()

# insertar una lista de usuarios
usuarios = [
    ('aaa@yahoo.com','Ramona Minerva','qwqasa'),
    ('ccchy@outlook.com','Catalina','jjass'),
    ('neggia@yahoo.com','Neyria','kiokk'),

]


cursor.executemany("INSERT INTO usuarios VALUES (null,?,?,?)", usuarios)
conexion.commit()


# borrar todos los registros
# cursor.execute("DELETE FROM usuarios")
# conexion.commit()




# cambiar/actualizar 
sql = " UPDATE usuarios SET username='Antonia Andrades' WHERE email LIKE 'aaa@yahoo.com'"
cursor.execute(sql)

sql = " UPDATE usuarios SET email='antonia_andrades@yahoo.com' WHERE email LIKE 'aaa@yahoo.com'"
cursor.execute(sql)

sql = " UPDATE usuarios SET password='123456' WHERE email LIKE 'neggia@yahoo.com'"
cursor.execute(sql)

# listar solamente usuarios de yahoo
#cursor.execute("SELECT * from usuarios WHERE email LIKE '%yahoo.com' ")
#usuarios = cursor.fetchall()

# listar todos los registros
cursor.execute("SELECT * from usuarios;")
usuarios = cursor.fetchall()

print('Email'+30*' '+'Usuario'+20*' '+'Contraseña')
print(5*'-'+30*' '+7*'-'+20*' '+10*'-')
for user in usuarios:
    print(user[1]+30*' '+
        user[2]+20*' '+
        user[3])
    


# cerrar el archivo
conexion.close()