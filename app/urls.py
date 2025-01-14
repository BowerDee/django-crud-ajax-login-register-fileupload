from .views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^createplayer$', create, name='createplayer'),
    url(r'^playerlist$', list, name='playerlist'),
    url(r'^editplayer/(?P<id>\d+)$', edit, name='editplayer'),
    url(r'^deleteaccount/(?P<id>\d+)$', deleteaccount, name='deleteaccount'),
    url(r'^deleteplayer/(?P<id>\d+)$', deleteplayer, name='deleteplayer'),
    url(r'^createquestion$', createquestion, name='createquestion'),
    url(r'^createbrand$', createbrand, name='createbrand'),
    url(r'^questionlist$', questionlist, name='questionlist'),
    url(r'^questionlistbydynasty$', questionlistbydynasty, name='questionlistbydynasty'),
    url(r'^editquestion/(?P<id>\d+)$', editquestion, name='editquestion'),
    url(r'^editquestion/editquestionid/(?P<id>\d+)$', editquestion, name='editquestionid'),
    url(r'^brandlist$', brandlist, name='brandlist'),
    url(r'^reward$', reward, name='reward'),
    url(r'^editbrand/(?P<id>\d+)$', editbrand, name='editbrand'),
    url(r'^editbrand/editbrandid/(?P<id>\d+)$', editbrandid, name='editbrandid'),
	
	
	url(r'^editreward/(?P<id>\d+)$', editreward, name='editreward'),
	url(r'^editreward/editrewardid/(?P<id>\d+)$', editrewardid, name='editreward'),
	
    url(r'^playercharts$', playercharts, name='playercharts'),
    url(r'^editplayer/editplayerinfo/(?P<id>\d+)$', editplayerinfo, name='editplayerinfo'),
    url(r'^deletebrand/(?P<id>\d+)$', deleteBrand, name='deletebrand'),
    url(r'^deletequestion/(?P<id>\d+)$', deletequestion, name='deletequestion'),
    url(r'^scorelist$', scorelist, name='scorelist'),
    url(r'^scorelistbydynasty$', scorelistbydynasty, name='scorelistbydynasty'),
]
