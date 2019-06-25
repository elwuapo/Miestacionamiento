from django.contrib import admin
from web.models import Estado, Estacionamiento, Cuenta, Contrato, Vehiculo

# Register your models here.
admin.site.register(Estado)
admin.site.register(Estacionamiento)
admin.site.register(Cuenta)
admin.site.register(Contrato)
admin.site.register(Vehiculo)