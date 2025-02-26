from django.shortcuts import render
from .models import navbaritem, libro, autor, categoria
from django.http import JsonResponse

# Create your views here.

def index(request):
    navbaritems = navbaritem.objects.all()
    context = {"navbaritems": navbaritems}
    return render(request, 'home/index.html', context)

def index2(request):
    navbaritems = navbaritem.objects.all()
    libros = libro.objects.all()
    query = request.GET.get('query', '')
    print(f"Query received: {query}") 
    if query:
        libros = libro.objects.filter(titulolib__iexact=query)
    else:
        libros = libro.objects.all()

    context = {"navbaritems": navbaritems, "libros": libros ,
        'query': query,}
    return render(request, 'catalogo_libro/index2.html', context)

def index3(request):
    navbaritems = navbaritem.objects.all()
    autors = autor.objects.all()
    context = {"navbaritems": navbaritems, "autors": autors}
    return render(request, 'catalago_autor/index3.html', context)

def index4(request):
    navbaritems = navbaritem.objects.all()
    categorias = categoria.objects.all()
    context = {"navbaritems": navbaritems, "categorias": categorias}
    return render(request, 'categorias/index4.html', context)

def index5(request):
    query = request.GET.get('query', '')
    print(f"Query received: {query}") 
    if query:
        libros = libro.objects.filter(titulolib__iexact=query)
    else:
        libros = libro.objects.all()
    context = {
        'libros': libros,
        'query': query,
    }
    return render(request, 'catalogo_libro/index2.html', context)