from django.db import models

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio_estimado = models.IntegerField(help_text="Precio en pesos chilenos")

    def __str__(self):
        return self.nombre

class Cotizacion(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    # Conectamos la cotización con el servicio que el cliente quiere
    servicio_solicitado = models.ForeignKey(Servicio, on_delete=models.SET_NULL, null=True)
    mensaje = models.TextField()
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, default='Pendiente', choices=[
        ('Pendiente', 'Pendiente'),
        ('Contactado', 'Contactado'),
        ('Rechazado', 'Rechazado'),
        ('Completado', 'Completado')
    ])

    def __str__(self):
        return f"Cotización de {self.nombre_cliente} - {self.fecha_solicitud.strftime('%d/%m/%Y')}"