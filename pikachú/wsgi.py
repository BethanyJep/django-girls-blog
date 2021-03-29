"""
WSGI config for pikachú project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pikachú.settings')

application = get_wsgi_application()

# import pikachú
# import waitress
# waitress.serve(pikachú.wsgifunc, port=8041, url_scheme='https')
# from pikachú.wsgi import blog
# application = blog(application)