import datetime
import hashlib
import usuarios.conexion as dbase


#print(database)

connect = dbase.conectar()
db = connect[0]
cur =  connect[1]


#  buffered=True, para muchas consultas utilizando el mismo cursor.

class Usuario:


    # constructor
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registrar(self):

        fecha = datetime.datetime.now()

        # cifrar la contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))


        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)


        try:
            cur.execute(sql, usuario)
            db.commit()
            result = [cur.rowcount, self]
        except:
            result = [0, self]


        return result


    def identificar(self):
        
        sql = "SELECT * from usuarios WHERE email = %s AND password = %s" 

        # clave cifrada 
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        # datos para la consulta
        usuario = (self.email, cifrado.hexdigest())

        cur.execute(sql, usuario)

        result = cur.fetchone()

        return result

