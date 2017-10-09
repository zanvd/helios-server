"""
Authentication URLs

Ben Adida (ben@adida.net)
"""

from django.conf.urls import *

from .views import *
from .auth_systems.password import password_login_view, password_forgotten_view
from .auth_systems.twitter import follow_view

urlpatterns = [
    # basic static stuff
    url(r'^$', index, name = 'helios_auth.views.index'),
    url(r'^logout$', logout, name = 'helios_auth.views.logout'),
    url(r'^start/(?P<system_name>.*)$', start, name = 'helios_auth.views.start'),
    # weird facebook constraint for trailing slash
    url(r'^after/$', after, name = 'helios_auth.views.after'),
    url(r'^why$', perms_why, name = 'helios_auth.views.perms_why'),
    url(r'^after_intervention$', after_intervention, name = 'helios_auth.views.after_intervention'),
    
    ## should make the following modular

    # password auth
    url(r'^password/login', password_login_view, name = 'helios_auth.views.password_login_view'),
    url(r'^password/forgot', password_forgotten_view, name = 'helios_auth.views.password_forgotten_view'),

    # twitter
    url(r'^twitter/follow', follow_view, name = 'helios_auth.views.follow_view'),
]
