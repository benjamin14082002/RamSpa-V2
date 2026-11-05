from django.shortcuts import render, redirect
from .models import Cotizacion
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.core.mail import send_mail
from django.conf import settings

def inicio(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre_cliente')
        correo = request.POST.get('email')
        fono = request.POST.get('telefono')
        texto = request.POST.get('mensaje')

        # 1. Guardamos en la base de datos MySQL
        Cotizacion.objects.create(
            nombre_cliente=nombre,
            email=correo,
            telefono=fono,
            mensaje=texto
        )
        
        # 2. Enviamos el correo automático (integración de plataforma de mensajería)
        asunto = f"Nueva Cotización Recibida - {nombre}"
        mensaje_email = (
            f"Has recibido una nueva solicitud de servicio en RAM SPA:\n\n"
            f"Cliente: {nombre}\n"
            f"Correo: {correo}\n"
            f"Teléfono: {fono}\n"
            f"Detalles del proyecto:\n{texto}\n\n"
            f"Revisa el panel de administración para gestionar este requerimiento."
        )
        
        try:
            send_mail(
                subject=asunto,
                message=mensaje_email,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['admin@ramspa.cl'], # Correo simulado de la administración
                fail_silently=True,
            )
        except Exception as e:
            print(f"Error al enviar correo: {e}")

        return redirect('inicio')
    
    return render(request, 'index.html')

def registro(request):
    if request.method == 'POST':
        usuario = request.POST.get('username')
        clave = request.POST.get('password')
        
        if not User.objects.filter(username=usuario).exists():
            nuevo_usuario = User.objects.create_user(username=usuario, password=clave)
            login(request, nuevo_usuario)
            return redirect('inicio')
            
    from django.contrib.auth.forms import UserCreationForm
    form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})