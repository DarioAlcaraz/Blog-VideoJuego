from django.contrib import admin
from .models import MensajeContacto

@admin.register(MensajeContacto)
class MensajeContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'fecha')
    search_fields = ('nombre', 'email', 'mensaje')
    list_filter = ('fecha',)
