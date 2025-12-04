from django.urls import path
from .views import * # el * es para traer todo lo que hay en las views

urlpatterns = [
    path("", ListProductView.as_view(),name="lista_productos"),
    path('camiseta/<int:pk>/', CamisetaDetailView.as_view(), name='camiseta_detail'),
    path('crear/', CamisetaCreateView.as_view(), name='camiseta_create'),
    path('editar/<int:pk>/', CamisetaUpdateView.as_view(), name='camiseta_update'),
    path('eliminar/<int:pk>/', CamisetaDeleteView.as_view(), name='camiseta_delete'),  
]