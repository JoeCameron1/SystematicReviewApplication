from django.conf.urls import patterns, url
from ultimatereview import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^register/$', views.register, name='register'),
                       url(r'^login/$', views.user_login, name='login'),
                       url(r'^myreviews/', views.myreviews, name='myreviews'),
                       url(r'^myprofile/', views.myprofile, name='myprofile'),
                       url(r'^logout/$', views.user_logout, name='logout'),
                       url(r'^query/$', views.indexQueried, name='query'),
                       )
