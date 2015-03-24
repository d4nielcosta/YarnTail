from django.conf.urls import patterns, include, url
from django.contrib import admin

from registration.backends.simple.views import RegistrationView

from yarntail import views
import settings


class MyRegistrationView(RegistrationView):
    def get_success_url(selfself,request, user):
        return '/yarntail/add_profile/'

urlpatterns = patterns('',
                       url(r'^$', views.index_popular, name='index_popular'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^yarntail/', include('yarntail.urls')),
                       url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
                       url(r'^accounts/', include('registration.backends.simple.urls')),
                       url(r'^search/', include('haystack.urls')),
                       )

handler400 = 'yarntail.views.handle404'
handler404 = 'yarntail.views.handle404'
handler500 = 'yarntail.views.handle404'

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',(r'^media/(?P<path>.*)','serve',{'document_root': settings.MEDIA_ROOT}), )