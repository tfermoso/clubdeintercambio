from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Libro,Prestamo

def index(request):
    if(request.session.get('usuario_id')): 
        #obtengo los libros que no son del usuario logeado y excluir los libros prestados (estado=3)
        libros_disponibles = Libro.objects.exclude(usuario_id=request.session.get('usuario_id')).exclude(libro_id__in=Prestamo.objects.filter(estado_id=3).values('libro_id'))           
        
        return render(request, 'prestamos/index.html', {'libros': libros_disponibles}) 
    else:
        #redirijo a la pagina de login
        return redirect('usuarios:login')
 
def solicitar(request, libro_id):
    libro = Libro.objects.get(libro_id=libro_id)
    #no solicitar libro ya solicitado
    if(Prestamo.objects.filter(libro_id=libro_id,estado_id=1)):
        return redirect('prestamos:index')
    prestamo = Prestamo(libro=libro, usuario_id=request.session.get('usuario_id'), estado_id=1)
    prestamo.save()
    return redirect('prestamos:index')  # Redirige a la lista de libros, por ejemplo.   
