from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *
from django.http import JsonResponse


# Create your views here.
def inicio(request):
    return render(request, 'core/inicio.html')

def libros(request):
    return render(request, 'core/libros.html')

def categorias(request):
    return render(request, 'core/categorias.html')

def autores(request):
    return render(request, 'core/autores.html')

def api_libros(request):
    libros = list(Libro.objects.values('nombre', 'autor', 'precio'))
    return JsonResponse(libros, safe=False)

def api_autores(request):
    autores = list(Autor.objects.values('nombre', 'nacionalidad'))
    return JsonResponse(autores, safe=False)

def api_categorias(request):
    categorias = list(Categoria.objects.values('nombre', 'descripcion'))
    return JsonResponse(categorias, safe=False)

def libro_detalle(request, id):
    libro = get_object_or_404(Libro, id=id)
    data = {
        'nombre': libro.nombre,
        'autor': libro.autor,
        'anio': libro.anio,
        'precio': libro.precio,
    }
    return JsonResponse(data)