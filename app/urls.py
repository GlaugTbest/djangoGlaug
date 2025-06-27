from django.contrib import admin
from django.urls import path
from .views import index, pag2
urlpatterns = [
    path('', index, name='index'),
    path('pagina2', pag2, name='pagina2'),
]

