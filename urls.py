# -*- coding: utf-8 -*-
from django.conf.urls import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.views.static import serve

urlpatterns = [
    # SHOULD BE REPLACED BY APACHE STATIC PATH
    url(r'static/auth/(?P<path>.*)$', serve, {'document_root' : settings.ROOT_PATH + '/helios_auth/media'}),
    url(r'static/helios/(?P<path>.*)$', serve, {'document_root' : settings.ROOT_PATH + '/helios/media'}),
    url(r'static/(?P<path>.*)$', serve, {'document_root' : settings.ROOT_PATH + '/server_ui/media'}),
]

urlpatterns += i18n_patterns(
    url(r'^auth/', include('helios_auth.urls')),
    url(r'^helios/', include('helios.urls')),

    url(r'booth/(?P<path>.*)$', serve, {'document_root' : settings.ROOT_PATH + '/heliosbooth'}, name = 'booth'),
    url(r'verifier/(?P<path>.*)$', serve, {'document_root' : settings.ROOT_PATH + '/heliosverifier'}, name = 'verifier'),

    url(r'^', include('server_ui.urls')),
)
