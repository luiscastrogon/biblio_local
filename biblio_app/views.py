from django.shortcuts import render
from .models import navbaritem, libro, autor, categorias

# Create your views here.

def index(request):
    navbaritems = navbaritem.objects.all()
    context = {"navbaritems": navbaritems}
    return render(request, 'home/index.html', context)

def index2(request):
    navbaritems = navbaritem.objects.all()
    libros = libro.object.all()
    context = {"navbaritems": navbaritems, "libros": libros}
    return render(request, 'catalogo_libro/index2.html', context)

def index3(request):
    navbaritems = navbaritem.objects.all()
    autors = autor.object.all()
    context = {"navbaritems": navbaritems, "autors": autors}
    return render(request, 'catalago_autor/index3.html', context)

def index4(request):
    navbaritems = navbaritem.objects.all()
    categoriass = categorias.object(all)
    context = {"navbaritems": navbaritems, "categoriass": categoriass}
    return render(request, 'categorias/index4.html', context)