class Persona:

    def __init__(self, nombre="", apellido="",
        edad="", direccion="", email=""):
        
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.direccion = direccion
        self.email = email

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def getApellido(self):
        return self.apellido

    def setEdad(self, edad):
        self.edad = edad

    def getEdad(self):
        return self.edad

    def setDireccion(self, direccion):
        self.direccion = direccion

    def getDireccion(self):
        return self.direccion

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email

    def getPersonalInfo(self):

        info = 5*"-" + " Personal Info " + 5*"-"
        info += "\n" + "Nombre: " + self.nombre
        info += "\n" + "Apellido: " + self.apellido
        info += "\n" + "Edad: " + str(self.edad)
        info += "\n" + "Direccion: " + self.direccion
        info += "\n" + "Email: " + self.email

        return info

# Herencia - parte 1
class Informatico(Persona):

    def __init__(self):
        
        self.experiencia = 5 
        self.lenguajes = "Python, Perl, Bash"
        self.idiomas = "Francés, Inglés"

    def getExperiencia(self):
        return self.experiencia

    def getLenguajes(self):
        return self.lenguajes

    def getIdiomas(self):
        return self.idiomas


class TecnicoDeRedes(Informatico):

    def __init__(self):

        # herencia de atributos de la clase padre
        super().__init__()
        
        self.experiencia = 5
        self.funciones = "Auditar redes"

    def auditarRedes(self):
        return "Estoy auditando una red"