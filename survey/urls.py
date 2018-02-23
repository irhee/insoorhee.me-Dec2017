from django.conf.urls import url, include
from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^result/(?P<vote_id>\d+)/$', views.vote),
    url(r'^result/$', views.result),

]
