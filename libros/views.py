from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Libro



def index(request):
    if(request.session.get('usuario_id')): 
        libros= Libro.objects.filter("usuario_id=request.session.get('usuario_id')")
        return render(request, 'index.html', {'libros': libros}) 
    else:
        #redirijo a la pagina de login
        return redirect('usuarios:login')
