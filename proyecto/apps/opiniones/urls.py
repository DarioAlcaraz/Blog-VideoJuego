from django.urls import path
from . import views
from .views import agregar_opinion, detalle_post

app_name = 'opiniones'

urlpatterns = [
    path('agregar/<int:post_id>/', agregar_opinion, name='agregar_opinion'),
    path('detalle/<int:post_id>/', detalle_post, name='detalle_post'),
    path('', views.lista_opiniones, name='lista_opiniones'),
]