from django.contrib import admin
from django.urls import path, include
from gestion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    
    # Rutas automáticas de Django para login/logout
    path('cuentas/', include('django.contrib.auth.urls')), 
    
    # Nuestra ruta personalizada para que los clientes se registren
    path('registro/', views.registro, name='registro'), 
]