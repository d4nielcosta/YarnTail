from django.conf.urls import patterns, url
from yarntail import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^index/$', views.index, name='index'),

                       url(r'^about_us/$', views.about, name='about'),
                       url(r'^search/(?P<query_slug>[\w\-]+)/$', views.search, name='search'),

                       #Profile Related
                       url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
                       url(r'^profile/(?P<username_slug>[\w\-]+)/$', views.profile, name='profile'),
                       url(r'add_profile/$', views.register_profile, name='add_profile'),

                       #Pattern Related
                       url(r'^pattern/(?P<username_slug>[\w\-]+)/(?P<pattern_slug>[\w\-]+)/$', views.pattern, name='pattern'),
                       url(r'^pattern_instructions/$', views.pattern_instructions, name='pattern_instructions'),
                       url(r'^upload_instructions/$', views.upload_instructions, name='upload_instructions'),
                       url(r'^add_pattern/$', views.add_pattern, name='add_pattern'),
                       )


#/(?P<username_slug>[\w\-]+)
