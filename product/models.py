from django.db import models
from django.contrib.auth.models import User

class Camiseta(models.Model):
    # Información básica de la camiseta
    nombre = models.CharField(
        max_length=200, 
        verbose_name="Nombre de la camiseta",
        help_text="Ej: Camiseta Barcelona 2024 Home"
    )
    
    # Equipo y detalles
    equipo = models.CharField(
        max_length=100, 
        verbose_name="Equipo"
    )
    
    temporada = models.CharField(
        max_length=50,
        verbose_name="Temporada",
        help_text="Ej: 2023-2024"
    )
    
    # Tallas disponibles
    TALLAS = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]
    
    talla = models.CharField(
        max_length=3,
        choices=TALLAS,
        verbose_name="Talla"
    )
    
    # Descripción breve
    descripcion = models.TextField(
        max_length=500,
        verbose_name="Descripción breve",
        help_text="Describe el estado, características, etc."
    )
    
    # Precio
    precio = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="Precio ($)"
    )
    
    # Imagen
    imagen = models.ImageField(
        upload_to='camisetas/',
        verbose_name="Imagen de la camiseta",
        help_text="Sube una foto clara de la camiseta"
    )
    

    # Fechas automáticas
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    # Estado del anuncio
    publicado = models.BooleanField(default=True, verbose_name="Publicado")
    vendido = models.BooleanField(default=False, verbose_name="Vendido")
    
    class Meta:
        verbose_name = "Camiseta"
        verbose_name_plural = "Camisetas"
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return f"{self.equipo} - {self.temporada} (Talla: {self.talla}) - ${self.precio}"
