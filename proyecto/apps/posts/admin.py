from django.contrib import admin
from .models import Categoria, Post

@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'titulo', 'subtitulo', 'fecha', 'texto',
        'activo', 'categoria', 'imagen', 'publicado'
    )
    search_fields = ('titulo', 'subtitulo', 'texto')
    list_filter = ('fecha', 'activo', 'categoria', 'publicado')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)