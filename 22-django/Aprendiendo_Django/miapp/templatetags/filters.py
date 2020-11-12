"""
  filtros personalizados

"""
from django import template

register = template.Library()

@register.filter(name='saludo')
def saludo(value):

    msg = ''
    if len(value) >= 10:
        msg = '<p>Tu nombre es muy largo | Ejemplo de Filtro personalizado</p>'
        msg += '<hr>'
    return f"<h2 style='background:green;color:white;'> Bienvenido, {value} </h2>"+msg