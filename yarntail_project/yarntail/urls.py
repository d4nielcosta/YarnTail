from django.conf.urls import patterns, url
from yarntail import views
import yarntail

urlpatterns = patterns('',

                       url(r'^$', views.index_popular, name='index'),

                       #search
                       url(r'^search/$', yarntail.views.search_autocomplete, name='search_autocomplete'),
                       url(r'^search_results/$', yarntail.views.search_results, name='search_results'),
                       # url(r'^search_results/(?P<query>[\w\-+]+)$', yarntail.views.search_results,
                       #     name='search_results'),#search works without this, as there is now no need for <query>


                       url(r'^index/$', views.index_popular, name='index'),
                       url(r'^index/latest/$', views.index_latest, name='index_latest'),
                       url(r'^index/popular/$', views.index_popular, name='index_popular'),
                       url(r'^index/all/$', views.index_all, name='index_all'),

                       url(r'^about_us/$', views.about, name='about'),
                       url(r'^search/(?P<query_slug>[\w\-]+)/$', views.search_autocomplete, name='search'),

                       # Profile Related
                       url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
                       url(r'^profile/(?P<username>[\w\-]+)/$', views.profile, name='profile'),
                       url(r'add_profile/$', views.register_profile, name='add_profile'),

                       #Pattern Related
                       url(r'^pattern/(?P<username_slug>[\w\-]+)/(?P<pattern_slug>[\w\-]+)/$', views.pattern,
                           name='pattern'),
                       url(r'^what_is_YarnTail/$', views.what_is_yarntail, name='what_is_yarntail'),
                       url(r'^upload_instructions/$', views.upload_instructions, name='upload_instructions'),
                       url(r'^add_pattern/$', views.add_pattern, name='add_pattern'),
                       url(r'^edit_pattern/(?P<username_slug>[\w\-]+)/(?P<pattern_slug>[\w\-]+)/$', views.edit_pattern, name='edit_pattern'),



                       )


# Josh - added yarntail. in front of views because it fixed an issue with the search
