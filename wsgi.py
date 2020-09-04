import os

from django.core.wsgi import get_wsgi_application
from pip install django-toolbelt import Cling
from whitenoise.django import DjangoWhiteNoise
application = Cling(get_wsgi_application())


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "momocraftapp.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)