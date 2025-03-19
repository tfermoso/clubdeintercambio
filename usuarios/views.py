from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegistroForm

def index(request):
    return HttpResponse("Hello, desde Usuarios.")

def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            # Si usas el sistema de autenticación de Django, aquí podrías cifrar la contraseña:
            # usuario.set_password(form.cleaned_data["password"])
            usuario.save()
            # Redirige a la página de login o a otra de éxito
            return redirect('login')
    else:
        form = RegistroForm()

    return render(request, "usuarios/registro.html", {"form": form})

def login(request):
    return HttpResponse("Hello, desde login.")

