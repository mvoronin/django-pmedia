from django.conf.urls import patterns, include, url
from django.contrib import admin
from gallery.views import private_media

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^private/media/', private_media)
)
