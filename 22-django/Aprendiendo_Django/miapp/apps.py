from django.apps import AppConfig


class MiappConfig(AppConfig):
    name = 'miapp'
    verbose_name='Mon prémiere aplicación'


"""  
 o Cambiar cómo se verá el nombre de la aplicación en el Panel de Admin.

    - verbose_name='Mi primera aplicación'

    Que archivos debo ajustar?
    
        -  miapp/apps.py  (este mismo archivo)
        -  miapp/settings
                ajustar en INSTALLED_APPS [
                    ...
                    ..
                    ...
                    'miapp.apps.MiappConfig'
                ]


"""




