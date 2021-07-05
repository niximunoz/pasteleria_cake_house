from django import contrib
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.

def home(request):
    
    productos = Producto.objects.all()
    data = {
        'productos' : productos
    }
    
    return render(request, 'app/home.html', data)

def registroProducto(request):
    
    data = {
        'form' : RegProductoForm()
    }
    if request.method == 'POST':
        formulario = RegProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto Agregado Correctamente")
            return redirect(to=listaProductos)
        else:
            data["form"] = formulario

    return render(request, 'app/registroProducto.html', data)

def listaProductos(request):
    
    producto = Producto.objects.all().order_by("id")
    data = {
        'producto' : producto
    }
    
    return render(request, 'app/listaProductos.html', data)

def modificarProducto(request, id):
    
    producto = get_object_or_404(Producto, id = id)
    
    data = {
        'form' : ModProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ModProductoForm(data=request.POST, instance=producto, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto Modificado Correctamente")
            return redirect(to=listaProductos)
        else:
            data["form"] = formulario
    
    return render(request, 'app/modificarProducto.html', data)

def eliminarProducto(request, id):
    
    producto = get_object_or_404(Producto, id = id)
    producto.delete()
    messages.success(request, "Producto Eliminado Correctamente")
    return redirect(to="listaProductos")
    
def registrarComuna(request):
    data = {
        'form' : RegComunaForm()
    }
    if request.method == 'POST':
        formulario = RegComunaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Comuna Agregada Correctamente")
            return redirect(to=listaComuna)
        else:
            data["form"] = formulario
    return render(request, 'app/registrarComuna.html', data)

def modificarComuna(request, id):
    comuna = get_object_or_404(Comuna, id = id)
    
    data = {
        'form' : RegComunaForm(instance=comuna)
    }
    if request.method == 'POST':
        formulario = ModComunaForm(data=request.POST, instance=comuna)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Comuna Modificada Correctamente")
            return redirect(to=listaComuna)
        else:
            data["form"] = formulario
    
    return render(request, 'app/modificarComuna.html', data)

def listaComuna(request):
    comuna = Comuna.objects.all().order_by("id")
    data = {
        'comuna' : comuna
    }
    return render(request, 'app/listaComunas.html', data)

def eliminarComuna(request, id):
    
    comuna = get_object_or_404(Comuna, id = id)
    comuna.delete()
    messages.success(request, "Comuna Eliminada Correctamente")
    return redirect(to=listaComuna)

def registroCliente(request):


    data = {
        'form' : RegClienteForm()
    }
    if request.method == 'POST':
        formulario = RegClienteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Cliente Registrado Correctamente")
            return redirect(to=listaClientes)
        else:
            data["form"] = formulario

    return render(request, 'app/registroUsuario.html', data)

def iniciarSesion(request):

    return render(request, 'app/iniciarSesion.html')

def listaClientes(request):

    clientes = Cliente.objects.all().order_by("rut")

    data = {
        'clientes' : clientes
    }
    return render(request, 'app/listaClientes.html', data)

def eliminarCliente(request, rut):
    
    usuario = get_object_or_404(Cliente, rut = rut)
    usuario.delete()
    messages.success(request, "Cliente Eliminado Correctamente")
    return redirect(to=listaClientes)

def modificarCliente(request, rut):
    
    usuario = get_object_or_404(Cliente, rut = rut)
    
    data = {
        'form' : ModClienteForm(instance=usuario)
    }
    if request.method == 'POST':
        formulario = ModClienteForm(data=request.POST, instance=usuario)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Cliente Modificado Correctamente")
            return redirect(to=listaClientes)
        else:
            data["form"] = formulario
    
    return render(request, 'app/modificarCliente.html', data)