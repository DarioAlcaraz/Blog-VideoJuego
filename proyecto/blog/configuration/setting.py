import os
from pathlib import Path

from django.urls import reverse_lazy

# 📁 Ruta base del proyecto (apunta a Proyecto_final/blog/)
BASE_DIR = Path(__file__).resolve().parent.parent.parent


AUTH_USER_MODEL = 'usuarios.Usuario'

LOGIN_URL = reverse_lazy('usuarios:iniciar_sesion')
LOGIN_REDIRECT_URL = reverse_lazy('inicio')
LOGOUT_REDIRECT_URL = reverse_lazy('inicio')

# 🔐 Claves y entorno
SECRET_KEY = 'django-insecure-((9jqcu_1+s-hyp%lf4+(aat!wd(y2v%$12o0h659w(&@ipaa8'
DEBUG = True
ALLOWED_HOSTS = []

# 🧩 Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 📦 Tus apps
    'apps.posts',
    'apps.usuarios',
    'apps.opiniones',
    'blog',
    
     
]

# 🧱 Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 🧭 Rutas principales
ROOT_URLCONF = 'blog.urls'
WSGI_APPLICATION = 'blog.wsgi.application'

# 🧠 Templates: busca en blog/templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 🔌 Servidor WSGI


# 🗃️ Base de datos SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 🔐 Validación de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 🌍 Internacionalización
LANGUAGE_CODE = 'es-ar'
TIME_ZONE = 'America/Argentina/Buenos_Aires'
USE_I18N = True
USE_TZ = True

# 📂 Archivos estáticos y multimedia
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]


# Archivos multimedia
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# 🔁 Redirecciones de autenticación


# 🔑 Campo primario por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'