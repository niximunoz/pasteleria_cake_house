from django import forms
from django.db.models import fields
from django.db.models.expressions import CombinedExpression, F
from django.forms.fields import CharField
from .models import *
from django.forms import ValidationError
import datetime

class RegProductoForm(forms.ModelForm):
    def clean_id(self):
        idProducto = self.cleaned_data["id"]
        existe = Producto.objects.filter(id = idProducto).exists()
        
        if existe:
            raise ValidationError("Este id ya esta siendo utilizado!")
        
        return idProducto
    
    nombre = forms.CharField(min_length=3, max_length=50)
    stock = forms.IntegerField(min_value=1, max_value=999999)
    precio_venta = forms.IntegerField(min_value=20, max_value=999999)
    imagen = forms.ImageField(required=False)

    
    class Meta:
        model = Producto
        fields = ['id','nombre', 'stock', 'precio_venta', 'descripcion']
    
class ModProductoForm(forms.ModelForm):

    nombre = forms.CharField(min_length=3, max_length=50)
    precio_Venta = forms.IntegerField(min_value=20, max_value=9999999)
    imagen = forms.ImageField(required=False)

    
    class Meta:
        model = Producto
        fields = ['id','nombre', 'stock', 'precio_venta', 'descripcion']
        
    
class RegComunaForm(forms.ModelForm):
    
    def clean_id(self):
        idComuna = self.cleaned_data["id"]
        existe = Comuna.objects.filter(id = idComuna).exists()
        
        if existe:
            raise ValidationError("Este id ya esta siendo utilizado!")
        
        return idComuna
    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        existe = Comuna.objects.filter(nombre = nombre).exists()
        
        if existe:
            raise ValidationError("Este Nombre de comuna ya esta registrada!")
        
        return nombre
    nombre = forms.CharField(min_length=1, max_length=50)
    id = forms.IntegerField(min_value=1, max_value=999)
    class Meta:
        model = Comuna
        fields = '__all__'
        

class ModComunaForm(forms.ModelForm):
    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        existe = Comuna.objects.filter(nombre = nombre).exists()
        
        if existe:
            raise ValidationError("Este Nombre de comuna ya esta registrado!")
        
        return nombre
    nombre = forms.CharField(min_length=1, max_length=50)
    id = forms.IntegerField(min_value=1, max_value=999)
    class Meta:
        model = Comuna
        fields = '__all__'

class RegClienteForm(forms.ModelForm):
    def clean_rut(self):
        rut = self.cleaned_data["rut"]
        existe = Cliente.objects.filter(rut = rut).exists()

        if existe:
            raise ValidationError("Este rut ya está registrado!")    
        return rut   
    def clean_email(self):
        email = self.cleaned_data["email"]
        existe = Cliente.objects.filter(email = email).exists()

        if existe:
            raise ValidationError("Este email ya está registrado!")    
        return email 
    def clean_fecha_de_Nacimiento(self):
        
        fecha = self.cleaned_data["fecha_de_Nacimiento"]
        if fecha > datetime.date.today():
            raise forms.ValidationError("Debes ingresar una fecha valida")
        return fecha 
    
    rut = forms.IntegerField(min_value=1000000, max_value=99999999)
    nombre = forms.CharField(min_length=3, max_length=50)
    apellido_paterno = forms.CharField(min_length=3, max_length=50)
    apellido_materno = forms.CharField(min_length=3, max_length=50)
    direccion = forms.CharField(min_length=3, max_length=50)
    
    class Meta:
        model = Cliente
        fields = ['rut', 'digito_verificador', 'nombre', 'apellido_Paterno', 'apellido_Materno', 'email', 'fecha_de_Nacimiento', 'comuna', 'direccion']
    
        widgets = {
            'fecha_de_Nacimiento' : forms.SelectDateWidget(years=range(1945, 2022))
        }
    

class ModClienteForm(forms.ModelForm):

    def clean_fecha_de_Nacimiento(self):
        
        fecha = self.cleaned_data["fecha_de_Nacimiento"]
        if fecha > datetime.date.today():
            raise forms.ValidationError("Debes ingresar una fecha valida")
        return fecha 

    rut = forms.IntegerField(min_value=1000000, max_value=99999999)
    nombre = forms.CharField(min_length=3, max_length=50)
    apellido_paterno = forms.CharField(min_length=3, max_length=50)
    apellido_materno = forms.CharField(min_length=3, max_length=50)
    direccion = forms.CharField(min_length=3, max_length=50)


    class Meta:
        model = Cliente
        fields = model = Cliente
        fields = ['rut', 'digito_verificador', 'nombre', 'apellido_Paterno', 'apellido_Materno', 'email', 'fecha_de_Nacimiento', 'comuna', 'direccion']

        widgets = {
            'fecha_de_Nacimiento' : forms.SelectDateWidget(years=range(1945, 2022)),
        }
        