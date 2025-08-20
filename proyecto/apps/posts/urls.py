from django.urls import path
from .views import ListarPosts, CrearPost, ActualizarPost, EliminarPost, DetallePost

app_name = 'posts'  # Esto permite usar {% url 'posts:crear_post' %} en templates

urlpatterns = [
    path('', ListarPosts.as_view(), name='posts'),  # Listado general
    path('crear/', CrearPost.as_view(), name='crear_post'),
    path('detalle/<int:pk>/', DetallePost.as_view(), name='detalle_post'),
    path('editar/<int:pk>/', ActualizarPost.as_view(), name='editar_post'),
    path('eliminar/<int:pk>/', EliminarPost.as_view(), name='eliminar_post'),
]