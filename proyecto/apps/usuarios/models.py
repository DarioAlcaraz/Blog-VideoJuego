from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class Usuario(AbstractUser):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField('Fecha de nacimiento', default='2000-01-01')
    es_colaborador = models.BooleanField('¿Es colaborador?', default=False)
    imagen = models.ImageField(
        upload_to='usuarios/',
        null=True,
        blank=True,
        default='usuarios/usuario_default.jpg'
    )
    genero = models.CharField(
        max_length=10,
        choices=[('M', 'Masculino'), ('F', 'Femenino')],
        verbose_name='Género'
    )

    class Meta:
        ordering = ('-nombre',)
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f'{self.username} ({self.nombre} {self.apellido})'

    def get_absolute_url(self):
        return reverse('inicio')

    def nombre_completo(self):
        return f'{self.nombre} {self.apellido}'
