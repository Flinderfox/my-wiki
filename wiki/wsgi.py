"""
WSGI config for wiki project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys

settings_path = '/home/Flinderfox/flinderfox.pythonanywhere.com'
sys.path.insert(0, settings_path)
if settings_path not in sys.path:
    sys.path.append(settings_path)

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wiki.settings')
os.environ['DJANGO_SETTINGS_MODULE'] = 'wiki.settings'

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
# application = get_wsgi_application()
application = StaticFilesHandler(get_wsgi_application())

"""
# This file contains the WSGI config
# uration required to serve up your
# Django app
import os
import sys

# Add your project directory to the sys.path
settings_path = '/home/Flinderfox/flinderfox.pythonanywhere.com'
sys.path.insert(0, settings_path)

# Set environment variable to tell django where your settings.py is
os.environ['DJANGO_SETTINGS_MODULE'] = 'wiki.settings'

# Set the 'application' variable to the Django wsgi app
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
"""