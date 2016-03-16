from django.conf.urls import patterns, url
from ultimatereview import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'))