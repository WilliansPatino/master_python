import clases

user1 = clases.Persona("Willians","Patiño", 56,
    "Caracas", "wjospi@gmail.com")


print(user1.getNombre())

user2 = clases.Persona()

user2.setNombre("Mine")

print(user2.getNombre())

user2.setApellido("Patiño")

print(user1.getPersonalInfo())
print(user2.getPersonalInfo())

user2.setEdad(13)
user2.setEmail("miner@gmail.com")
print(user2.getPersonalInfo())

# comprobar tipado de objeto
if type(user2) == clases.Persona:
    print("Es un objeto de clase")

#  herencia - parte 2
informatico = clases.Informatico()
informatico.setNombre("Willians")
informatico.setEdad(55)
informatico.setEmail("gmail.com")
informatico.setDireccion("Suiza")

print(f" El informatico se llama {informatico.getNombre()} y su email es {informatico.getEmail()}")
print(f"Domina estos lenguajes: {informatico.getLenguajes()}")
print(f"Vive en {informatico.getDireccion()}")
print(f"Idiomas: {informatico.getIdiomas()}")

# TECNICO
tecnico = clases.TecnicoDeRedes()
print("--- CLASE: TECNICO --")
print(tecnico.auditarRedes())
print(tecnico.experiencia)
print(tecnico.getIdiomas())

tecnico.set