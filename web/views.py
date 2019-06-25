from django.shortcuts import render, redirect
from web.models import Estacionamiento, Estado, Cuenta, Contrato, Vehiculo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as auth_login
# Create your views here.

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# METODOS DE VISUALIZADO DE PAGINA

def mostrarInicio(request):
    return render(request,'inicio.html')

def mostrarLogin(request):
    return render(request, 'login.html')

def mostrarCuenta(request):

    user = request.user.id
    cuenta = Cuenta.objects.get(usuario = user)

    return render(request,'cuenta.html', {'cuenta':cuenta})

def mostrarEstacionamientos(request):
    estacionamientos = Estacionamiento.objects.all()
    return render(request, 'contratar.html',{'estacionamientos':estacionamientos})

def mostrarTransbank(request):
    codigo = request.POST.get('pago_codigo','')

    estacionamiento = Estacionamiento.objects.get(codigo = codigo)

    return render(request, 'pagar.html', {'estacionamiento': estacionamiento})
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# METODOS FUNCIONES

def crearUsuario(request):

    usuario = request.POST.get('registro_usuario','')
    contraseña = request.POST.get('registro_contraseña','')

    user = User.objects.create_user(username = usuario, password = contraseña)
    user.save()
    
    vehiculo = Vehiculo.objects.get(patente = "XX XX 99")
    cuenta = Cuenta(usuario = user, vehiculo = vehiculo)
    cuenta.save()


    return render(request,'login.html')

def iniciarSesion(request):

    username = request.POST.get('login_usuario','')
    password = request.POST.get('login_contraseña', '')
    

    usuario = authenticate(request, username = username, password = password)

    if usuario is not None:
        auth_login(request, usuario)
        return redirect('mostrarInicio')
    else:
        return redirect('mostrarLogin')

def cerrarSesion(request):
    logout(request)
    return redirect('mostrarInicio')

def crearEstacionamiento(request):

    usuario = request.POST.get('usuario','')
    direccion = request.POST.get('direccion', '')
    latitud = request.POST.get('latitud', '')
    longitud = request.POST.get('longitud', '')
    precio = request.POST.get('precio', '')

    user = User.objects.get(username = usuario)
    cuenta = Cuenta.objects.get(usuario = user)
    estado = Estado.objects.get(nombre = "Disponible")

    estacionamiento = Estacionamiento(usuario = user, direccion = direccion, latitud = latitud, longitud = longitud, precio = precio, estado = estado)
    estacionamiento.save()

    cuenta.estacionamientos.add(estacionamiento)
    

    return redirect('mostrarInicio')

def crearContrato(request):

    usuario_propietario = request.POST.get('contrato_propietario','')
    usuario_arrendador = request.POST.get('contrato_arrendador','')
    codigo_estacionamiento = request.POST.get('contrato_codigo_estacionamiento','')

    propietario = User.objects.get(username = usuario_propietario)
    arrendador = User.objects.get(username = usuario_arrendador)
    estacionamiento = Estacionamiento.objects.get(codigo = codigo_estacionamiento)

    

    contrato = Contrato(propietario = propietario, arrendador = arrendador, estacionamiento = estacionamiento)
    contrato.save()

    cuentaPropietario = Cuenta.objects.get(usuario = propietario)
    cuentaArrendador = Cuenta.objects.get(usuario = arrendador)

    cuentaPropietario.contratos.add(contrato)
    cuentaArrendador.contratos.add(contrato)

    return redirect('mostrarCuenta')

def editarEstacionamiento(request):

    codigo = request.POST.get('edit_codigo','')
    propietario = request.POST.get('edit_usuario','')
    direccion = request.POST.get('edit_direccion','')
    latitud = request.POST.get('edit_latitud','')
    longitud = request.POST.get('edit_longitud','')
    precio = request.POST.get('edit_precio','')
    estado = request.POST.get('edit_estado','')
    img = request.POST.get('edit_img','')

    valor = Estado.objects.get(nombre = estado)

    estacionamiento = Estacionamiento.objects.get(codigo = codigo)

    estacionamiento.direccion = direccion
    estacionamiento.latitud = latitud
    estacionamiento.longitud = longitud
    estacionamiento.precio = precio
    estacionamiento.estado = valor
    estacionamiento.img = img

    estacionamiento.save()

    return redirect('mostrarCuenta')

def realizarPago(request):

    codigo = request.POST.get('pagar_codigo_estacionamiento','')

    estacionamiento = Estacionamiento.objects.get(codigo = codigo)
    
    estado = Estado.objects.get(nombre = "En uso")

    estacionamiento.estado = estado

    estacionamiento.save()
    
    return redirect('mostrarCuenta')

def editarCuenta(request):

    user = request.user.id
    cuenta = Cuenta.objects.get(usuario = user)

    direccion = request.POST.get('cuenta_direccion','')
    numero = request.POST.get('cuenta_numero','')
    img = request.POST.get('cuenta_img','')

    cuenta.direccion = direccion
    cuenta.numero = numero
    cuenta.img = img

    cuenta.save()

    return redirect('mostrarCuenta')

def editarAuto(request):

    user = request.user.id
    cuenta = Cuenta.objects.get(usuario = user)

    patente = request.POST.get('cuenta_patente','')
    marca = request.POST.get('cuenta_marca','')
    color = request.POST.get('cuenta_color','')
    img = request.POST.get('cuenta_img_a','')

    

    if(patente == "XX XX 99"):
        
        vehiculo = Vehiculo.objects.get(patente = patente)
        vehiculo.patente = patente
        vehiculo.marca = marca
        vehiculo.color = color
        vehiculo.img = img

        vehiculo.save()
    else:
        vehiculo = Vehiculo(patente = patente, marca = marca, color = color, img = img)
        vehiculo.save()
        
        cuenta.vehiculo = vehiculo
        cuenta.save()

    return redirect('mostrarCuenta')