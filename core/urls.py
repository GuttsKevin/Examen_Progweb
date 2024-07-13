from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('libros/', libros, name='libros'),
    path('categorias/', categorias, name='categorias'),
    path('autores/', autores, name='autores'),
    path('api/libros/', api_libros, name='api_libros'),
    path('api/autores/', api_autores, name='api_autores'),
    path('api/categorias/', api_categorias, name='api_categorias'),
    path('api/libros/<int:id>/', libro_detalle, name='libro_detalle'),
]