from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from gallery.views import private_media, Gallery

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^private/media/', private_media),
    url(r'^gallery/$', Gallery.as_view(), name='gallery')
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
