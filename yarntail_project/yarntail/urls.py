from django.conf.urls import patterns, url
import yarntail

urlpatterns = patterns('',

                       url(r'^$', yarntail.views.index, name='index'),
                       url(r'^index/$', yarntail.views.index, name='index'),

                       url(r'^$', views.index_popular, name='index'),
                       url(r'^index/$', views.index_popular, name='index'),
                       url(r'^index/latest/$', views.index_latest, name='index_latest'),
                       url(r'^index/popular/$', views.index_popular, name='index_popular'),
                       url(r'^index/all/$', views.index_all, name='index_all'),


                       url(r'^about_us/$', yarntail.views.about, name='about'),
                       url(r'^search/(?P<query_slug>[\w\-]+)/$', yarntail.views.search, name='search'),

                       #Profile Related
                       url(r'^profile/edit/$', yarntail.views.edit_profile, name='edit_profile'),
                       url(r'^profile/(?P<username_slug>[\w\-]+)/$', yarntail.views.profile, name='profile'),
                       url(r'add_profile/$', yarntail.views.register_profile, name='add_profile'),

                       #Pattern Related

                       url(r'^pattern/(?P<username_slug>[\w\-]+)/(?P<pattern_slug>[\w\-]+)/$', yarntail.views.pattern, name='pattern'),
                       url(r'^pattern_instructions/$', yarntail.views.pattern_instructions, name='pattern_instructions'),
                       url(r'^upload_instructions/$', yarntail.views.upload_instructions, name='upload_instructions'),
                       url(r'^add_pattern/$', yarntail.views.add_pattern, name='add_pattern'),
                       url(r'^search/$', yarntail.views.search, name='search'),
                       url(r'^search_results/$', yarntail.views.search_results, name='search_results'),
                       url(r'^search_results/(?P<query>[\w\-]+)$', yarntail.views.search_results, name='search_results'),

                       url(r'^pattern/(?P<username_slug>[\w\-]+)/(?P<pattern_slug>[\w\-]+)/$', views.pattern, name='pattern'),
                       url(r'^pattern_instructions/$', views.pattern_instructions, name='pattern_instructions'),
                       url(r'^upload_instructions/$', views.upload_instructions, name='upload_instructions'),
                       url(r'^add_pattern/$', views.add_pattern, name='add_pattern'),

                       #Comment
                   #    url(r'^pattern/(?P<username_slug>[\w\-]+)/(?P<pattern_slug>[\w\-]+)/add_comment/$', views.comment, name='add_comment'),

                       )


#Josh - added yarntail. in front of views because it fixed an issue with the search
