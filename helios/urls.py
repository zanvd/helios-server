# -*- coding: utf-8 -*-
from django.conf.urls import *

from django.conf import settings

from .views import *

urlpatterns = None

urlpatterns = [
  url(r'^autologin$', admin_autologin, name = 'helios.views.admin_autologin'),
  url(r'^testcookie$', test_cookie, name = 'helios.views.test_cookie'),
  url(r'^testcookie_2$', test_cookie_2, name = 'helios.views.test_cookie_2'),
  url(r'^nocookies$', nocookies, name = 'helios.views.nocookies'),
  url(r'^stats/', include('helios.stats_urls')),

  # election shortcut by shortname
  url(r'^e/(?P<election_short_name>[^/]+)$', election_shortcut, name = 'helios.views.election_shortcut'),
  url(r'^e/(?P<election_short_name>[^/]+)/vote$', election_vote_shortcut, name = 'helios.views.election_vote_shortcut'),

  # vote shortcut
  url(r'^v/(?P<vote_tinyhash>[^/]+)$', castvote_shortcut, name = 'helios.views.castvote_shortcut'),
  
  # trustee login
  url(r'^t/(?P<election_short_name>[^/]+)/(?P<trustee_email>[^/]+)/(?P<trustee_secret>[^/]+)$', trustee_login, name = 'helios.views.trustee_login'),
  
  # electio
  url(r'^elections/params$', election_params, name = 'helios.views.election_params'),
  url(r'^elections/verifier$', election_verifier, name = 'helios.views.election_verifier'),
  url(r'^elections/single_ballot_verifier$', election_single_ballot_verifier, name = 'helios.views.election_single_ballot_verifier'),
  url(r'^elections/new$', election_new, name = 'helios.views.election_new'),
  url(r'^elections/administered$', elections_administered, name = 'helios.views.elections_administered'),
  url(r'^elections/voted$', elections_voted, name = 'helios.views.elections_voted'),
  
  url(r'^elections/(?P<election_uuid>[^/]+)', include('helios.election_urls')),
  
]


