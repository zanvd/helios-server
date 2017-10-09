# -*- coding: utf-8 -*-
from django.conf.urls import *

from .views import *

urlpatterns = [
  url(r'^$', home),
  url(r'^about$', about),
  url(r'^docs$', docs),
  url(r'^faq$', faq),
  url(r'^privacy$', privacy),
]
