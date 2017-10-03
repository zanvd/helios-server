"""
Helios URLs for Election related stuff

Ben Adida (ben@adida.net)
"""

from django.conf.urls import *

from helios.stats_views import *

urlpatterns = [
    url(r'^$', home, name = 'helios.stats_views.home'),
    url(r'^force-queue$', force_queue, name = 'helios.stats_views.force_queue'),
    url(r'^elections$', elections, name = 'helios.stats_views.elections'),
    url(r'^problem-elections$', recent_problem_elections, name = 'helios.stats_views.recent_problem_elections'),
    url(r'^recent-votes$', recent_votes, name = 'helios.stats_views.recent_votes'),
]
