from django.db import models

# Create your models here.


#/* aqui pequeñas clases */

class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(default='null', verbose_name='Imagén', 
        upload_to='articles')
    public = models.BooleanField(verbose_name='Publico/Privado')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado')

    #   De esta manera, cambio el nombre a los modelos  otros 
    class Meta:
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'
        # ordering = ['-id']
        ordering = ['-created_at']

    def __str__(self):
        
        if self.public:
            msg = 'Publicado'
        else:
            msg = 'Privado'

        return f'({self.id}) {self.title}  creado el {self.created_at} - [{msg}]'

"""
    o Cambiar como se mostrará el campo
    
        ... models.CharField(..., verbose_name='nuevo-nombre')

        image = models.ImageField() / ej. campo de imagen

    o Cambiar el nombre del objeto en el panel (buscar como magic method)

        def __str__(self):
            return ...

    o Para trabajar y manipular imagenes en Django Administration y Python

        agregar en el campo imagen:

            ... = models.ImageField(... , upload_to='articles')
---

   Si se desea indicar otra DB/Table 

     class Meta:
         db_table = "dbname"

    Es necesario hacer la migraciones y SQL migrate
---

# auto_now_add=True  // Guarda automaticamente la fecha
# DateTimeField // dato de fechas mas completo.
# DateField()  // entrada de fecha manual
"""


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