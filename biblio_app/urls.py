from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.index, name="index"),
 	path('catalogo_libro', views.index2, name="index2"),
  	path('catalogo_autor', views.index3, name="index3"),
   	path('categorias', views.index4, name="index4"),
]