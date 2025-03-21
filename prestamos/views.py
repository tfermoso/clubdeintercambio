from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Libro

def index(request):
    if(request.session.get('usuario_id')): 
        #obtengo los libros que no son del usuario logeado
        libros_disponibles = Libro.objects.exclude(usuario_id=request.session.get('usuario_id')) 
        
        return render(request, 'prestamos/index.html', {'libros': libros_disponibles}) 
    else:
        #redirijo a la pagina de login
        return redirect('usuarios:login')
    
