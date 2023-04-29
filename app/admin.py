from django.contrib import admin

from app.models import Cliente, Mensajero, Sucursal, Ciudad

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Mensajero)
admin.site.register(Sucursal)
admin.site.register(Ciudad)