from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Camiseta # el punto indica que es de la misma app(se puede poner tmb product.models)

class ListProductView(ListView):
    model = Camiseta
    template_name = "home.html"
    context_object_name = "Camisetas"

class CamisetaDetailView(DetailView):
    model = Camiseta
    template_name = 'detail_product.html'
    context_object_name = 'camiseta'

# DELETE VIEW - Eliminar camiseta
class CamisetaDeleteView(DeleteView):
    model = Camiseta
    template_name = 'delete_product.html'
    success_url = reverse_lazy("lista_productos")
    success_message = "¡Camiseta eliminada exitosamente!"

# UPDATE VIEW - Editar camiseta existente
class CamisetaUpdateView(UpdateView):
    model = Camiseta
    template_name = 'update_product.html'
    success_url = reverse_lazy("lista_productos")
    success_message = "¡Camiseta actualizada exitosamente!"
    fields = [
        'nombre',
        'equipo',
        'temporada', 
        'talla',
        'descripcion',
        'precio',
        'imagen',
        'publicado',
        'vendido'
    ]

# CREATE VIEW - Crear nueva camiseta
class CamisetaCreateView(CreateView):
    model = Camiseta
    template_name = 'create_product.html'
    success_url = reverse_lazy("lista_productos")
    success_message = "¡Camiseta creada exitosamente!"
    fields = [
        'nombre',
        'equipo', 
        'temporada',
        'talla',
        'descripcion',
        'precio',
        'imagen',
        'publicado'
    ]

