from django.conf.urls import patterns, include, url
from restfm import views 
from rest_framework.urlpatterns import format_suffix_patterns
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
             
    # Examples:
     url(r'^restfm/$', views.ApiView.as_view()),
    # url(r'^$', 'play.views.home', name='home'),
    # url(r'^play/', include('play.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns = format_suffix_patterns(urlpatterns)
