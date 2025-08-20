import os

# Usa 'local' si no se especifica, o 'prod' si se configura por variable de entorno
ENVIRONMENT = os.getenv('DJANGO_ENVIRONMENT', 'local')

if ENVIRONMENT == 'local':
    from .local import *
elif ENVIRONMENT == 'prod':
    from .prod import *