
from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'username', 'nombre', 'apellido', 'email',
        'fecha_nacimiento', 'genero', 'es_colaborador', 'mostrar_imagen'
    )
    search_fields = ('username', 'nombre', 'apellido', 'email')
    list_filter = ('genero', 'es_colaborador', 'fecha_nacimiento')
    readonly_fields = ('mostrar_imagen',)

    fieldsets = (
        ('Datos de acceso', {
            'fields': ('username', 'email', 'password')
        }),
        ('Información personal', {
            'fields': ('nombre', 'apellido', 'fecha_nacimiento', 'genero', 'imagen', 'mostrar_imagen')
        }),
        ('Permisos', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Fechas importantes', {
            'fields': ('last_login', 'date_joined')
        }),
    )

    def mostrar_imagen(self, obj):
        if obj.imagen:
            return f'<img src="{obj.imagen.url}" width="50" style="border-radius: 50%;">'
        return 'Sin imagen'
    mostrar_imagen.allow_tags = True
    mostrar_imagen.short_description = 'Foto de perfil'

    