from .views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^createplayer$', create, name='createplayer'),
    url(r'^playerlist$', list, name='playerlist'),
    url(r'^editplayer/(?P<id>\d+)$', edit, name='editplayer'),
    url(r'^createquestion$', createquestion, name='createquestion'),
    url(r'^queationlist$', queationlist, name='queationlist'),
    url(r'^editquestion/(?P<id>\d+)$', editquestion, name='editquestion'),
]