import os
import sys
sys.path.insert(0, '/var/evolitve-helios')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "local_settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
