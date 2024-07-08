from django.contrib import admin
from .models import autor, categoria, libro, navbaritem

# Register your models here.

admin.site.register(navbaritem)
admin.site.register(libro)
admin.site.register(autor)
admin.site.register(categoria)
