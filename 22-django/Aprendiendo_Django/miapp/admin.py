from django.contrib import admin

""" importar los modelos de mi proyecto de desarrollo """
from .models import Article, Category

# Register your models here.
""" Registrar los modelos con el objeto de generar un CRUD en el
    panel de administracion. Agregar estas clases. Despues, ir 
    al navegador, actualizar la pagina del panel
"""
# admin.site.register(Article)
admin.site.register(Category)

""" que campos son solo de lectura para luego mostrar """
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Article, ArticleAdmin)


# AJustar el título del panel de administraciòn
title_panel = "Master en Python & django | Willians Patiño"
admin.site.site_header = title_panel
admin.site.site_title = title_panel
admin.site.index_title = "Panel de gestión"