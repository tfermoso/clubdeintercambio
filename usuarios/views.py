from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegistroForm
from django.contrib.auth import authenticate, login

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

    return render(request, "registro.html", {"form": form})

def login(request):
    error = None
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        # Si tu autenticación usa el email como username, de lo contrario, deberás ajustarlo
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirige a la página principal u otra de tu elección
        else:
            error = "Email o contraseña incorrectos."
    
    return render(request, "usuarios/login.html", {"error": error})

