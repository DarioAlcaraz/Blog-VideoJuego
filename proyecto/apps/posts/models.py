from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

class Categoria(models.Model):
    nombre = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    subtitulo = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    texto = models.TextField(null=False)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    imagen = models.ImageField(upload_to='posts/', null=True, blank=True, default='posts/imagen_default.jpeg')
    publicado = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    def delete(self, using=None, keep_parents=False):
        if self.imagen:
            self.imagen.delete(save=False)
        super().delete(using=using, keep_parents=keep_parents)

    class Meta:
        ordering = ('-publicado',)