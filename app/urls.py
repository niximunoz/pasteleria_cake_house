from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    
    path('iniciarSesion/', iniciarSesion, name="iniciarSesion"),

    path('listaClientes/', listaClientes, name="listaClientes"),

    path('eliminarCliente/<rut>', eliminarCliente, name="eliminarCliente"),

    path('modificarCliente/<rut>', modificarCliente, name="modificarCliente"),
    
    path('registroProducto/', registroProducto, name="registroProducto"),
    
    path('listaProductos/', listaProductos, name="listaProductos"),
    
    path('registroUsuario/', registroCliente, name="registroUsuario"),


    path('registrarComuna/', registrarComuna, name="registrarComuna"),
    
    path('listaComunas/', listaComuna, name="listaComunas"),
    
    path('modificarComuna/<id>/', modificarComuna, name="modificarComuna"),
    
    path('eliminarComuna/<id>/', eliminarComuna, name="eliminarComuna"),
    
    path('modificarProducto/<id>/', modificarProducto, 
    name="modificarProducto"),
    
    path('eliminarProducto/<id>/', eliminarProducto, 
    name="eliminarProducto")
    

]