from django.contrib import admin

# Register your models here.
from core.Producto.models import Producto

admin.site.register(Producto)