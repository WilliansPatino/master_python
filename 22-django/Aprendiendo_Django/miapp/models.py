from django.db import models

# Create your models here.


#/* aqui pequeñas clases */



class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(default='null')
    public = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
"""
image = models.ImageField() / ej. campo de imagen
 """

# auto_now_add=True  // Guarda automaticamente la fecha
# DateTimeField // dato de fechas mas completo.
# DateField()  // entrada de fecha manual

class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    created_at = models.DateField()

# estas clases representan las tables de las bases de 
# datos.
# a partir de aca, crear base de dato
"""
paso siguientes: 
    1) importar/agregar mis apps en settings/INSTALLED_APPS
    2) crear una migracion (folder de referencia: migrations)
      
        $ python3 manage.py makemigrations
      
    3) General SQL de acuerdo al numero de migracion

        $ python3 manage.py sqlmigrate miapp 0001

    4) Guardar en la bases de datos

        $ python3 manage.py migrate

Nota:  Este es el procedimiento para creacion inicial y 
        para aplicar cambios en los modelos/tablas.

"""