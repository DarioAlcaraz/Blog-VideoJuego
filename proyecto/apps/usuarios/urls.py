from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from .views import ( RegistroUsuario,ActualizarUsuario,EliminarUsuario,listar_usuarios)
from . import views

from .views import CustomLoginView

app_name = 'usuarios'  # Esto permite usar {% url 'usuarios:nombre' %} en plantillas

urlpatterns = [
    path('', views.index, name='inicio'),
    path("registrar/", RegistroUsuario.as_view(), name='registrar'),
    path("iniciar_sesion/", CustomLoginView.as_view(), name='iniciar_sesion'),
    path("cerrar_sesion/", LogoutView.as_view(next_page='usuarios:iniciar_sesion'), name='cerrar_sesion'),
    path("actualizar_usuario/<int:pk>/", ActualizarUsuario.as_view(), name='actualizar_usuario'),
    path("listar_usuario/", listar_usuarios, name='listar_usuario'),
    path("eliminar_usuario/<int:pk>/", EliminarUsuario.as_view(), name='eliminar_usuario'),
    
]






