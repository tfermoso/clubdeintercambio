from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, desde Usuarios.")

def registro(request):
    return HttpResponse("Hello, desde Registro.")

def login(request):
    return HttpResponse("Hello, desde login.")

