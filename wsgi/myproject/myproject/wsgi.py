"""
WSGI config for myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

virtenv = os.path.join(os.environ['OPENSHIFT_PYTHON_DIR'], 'virtenv')
virtualenv = os.path.join(virtenv, 'bin', 'activate_this.py')

try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass


from yourproject.wsgi import application
from django.core.wsgi import get_wsgi_application




# GETTING-STARTED: change 'myproject' to your project name:
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")






application = get_wsgi_application()
