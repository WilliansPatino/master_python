"""
    Formularios basado en Clases. 9h07, 13.11.2020
"""
from django import forms

# agrega validacion
from django.core import validators


class formArticle(forms.Form):

    title = forms.CharField(
        label = 'Título',
        max_length=64,
        required=True,
        widget=forms.TextInput(
            attrs={
            'placeholder': 'Escribe un título de referencia, al menos de 5 caracteres',
            'class': 'titulo_form_article'
            }
        ),
        validators=[
            validators.MinLengthValidator(4, 'Título demasiado corto'),
            # validators.RegexValidator('^[A-Za-z0-9ñíóúéá]*$',
            # 'Incluya solo letras y números', 'invalid_title')
        ]
    )

    content = forms.CharField(
        label = 'Contenido',
        required=False,
        widget=forms.Textarea(
            # attrs={
            # 'placeholder': 'Escriba una descripción detallada',
            # 'class': 'titulo_form_article'
            # }
        ),
        validators=[
            validators.MaxLengthValidator(128, 'Contenido supera limite de caracteres')
        ]
    )

    # otra manera de definir atributos para el  campo
    content.widget.attrs.update({
        'placeholder': 'Escriba una descripción detallada',
        'class': 'titulo_form_article',
        'id': 'contenido_form'
    })

    public_options = [
        (1, 'Sí'),
        (0, 'No')
    ]

    public = forms.TypedChoiceField(
        label = '¿Público?',
        choices = public_options
    )