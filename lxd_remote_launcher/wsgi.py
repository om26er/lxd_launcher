import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lxd_remote_launcher.settings")

application = get_wsgi_application()
