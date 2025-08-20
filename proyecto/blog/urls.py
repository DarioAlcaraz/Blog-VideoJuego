from django.contrib import admin
from django.urls import path, include
from .views import Contacto
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from blog.views import HomeViews
from .views import nosotros_view


urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    path('inicio/', HomeViews.as_view()),

    # Página principal
    path('', HomeViews.as_view(), name='inicio'),

    # Contacto
    path('contacto/', Contacto, name='contacto'),
    path('nosotros/', nosotros_view, name = 'nosotros'),#agregado
    # Autenticación
    path('logout/', LogoutView.as_view(next_page='/usuarios/login/'), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),

    # Apps
    path('posts/', include('apps.posts.urls')),
    path('usuarios/', include('apps.usuarios.urls')),
    path('opiniones/', include('apps.opiniones.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




