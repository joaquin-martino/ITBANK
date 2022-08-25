from django.contrib import admin

from .models import Prestamo

# Register your models here. Nota: aca registramos los modelos para que aparezcan en el admin de django
admin.site.register(Prestamo)