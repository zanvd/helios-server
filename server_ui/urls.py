# -*- coding: utf-8 -*-
from django.conf.urls import *

from .views import *

urlpatterns = [
  url(r'^$', home, name = 'server_ui.views.home'),
  url(r'^about$', about, name = 'server_ui.views.about'),
  url(r'^docs$', docs, name = 'server_ui.views.docs'),
  url(r'^faq$', faq, name = 'server_ui.views.faq'),
  url(r'^privacy$', privacy, name = 'server_ui.views.privacy'),
]
