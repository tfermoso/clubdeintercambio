from django.shortcuts import render,redirect
from django.http import HttpResponse



def index(request):
    if(request.session.get('usuario_id')): 
        nombre=request.session.get('nombre')
        return render(request, 'index.html', {'nombre': nombre}) 
    else:
        #redirijo a la pagina de login
        return redirect('usuarios:login')
