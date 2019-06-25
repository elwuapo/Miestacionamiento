from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # INICIO
    path('', views.mostrarInicio, name="mostrarInicio"),

    # LOGIN AND REGIST
    path('login', views.mostrarLogin, name="mostrarLogin"),
    path('crear/usuario', views.crearUsuario, name="crearUsuario"),
    path('iniciar', views.iniciarSesion, name="iniciarSesion"),
    path('salir', views.cerrarSesion, name="cerrarSesion"),

    # REGISTRAR ESTACIONAMIENTO
    path('crear/estacionamiento', views.crearEstacionamiento, name="crearEstacionamiento"),

    # MOSTRAR CUENTA
    path('cuenta', views.mostrarCuenta, name="mostrarCuenta"),
    path('estacionamientos', views.mostrarEstacionamientos, name="mostrarEstacionamientos"),

    path('crear/contrato', views.crearContrato, name="crearContrato"),
    path('editar/estacionamiento', views.editarEstacionamiento, name="editarEstacionamiento"),
    path('pagar', views.realizarPago, name="realizarPago"),
    path('webpay', views.mostrarTransbank, name="mostrarTransbank"),

    path('editar/cuenta', views.editarCuenta, name="editarCuenta"),
    path('editar/auto', views.editarAuto, name="editarAuto"),

] + static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)