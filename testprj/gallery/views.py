# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
from urlparse import urlparse
from django.conf import settings
from django.http import HttpResponseForbidden, HttpResponse
from gallery.models import Photo

logger = logging.getLogger(__name__)


def private_media(request):
    if not request.user.is_authenticated():
        logger.debug("You haven't access to the file '%s'. User isn't authenticated!" % request.path)
        return HttpResponseForbidden()

    access_flag = False

    if request.user.has_perm('view_private_files'):
        access_flag = True
    else:
        logger.debug("You haven't access to the file '%s'. User hasn't permission '%s'!" %
                     (request.path, 'view_private_files'))

    if not access_flag:
        pfile = Photo.objects.get(file=request.path[len(settings.PRIVATE_MEDIA_URL)-1:])
        if request.user.pk == pfile.owner.pk:
            access_flag = True

    if not access_flag:
        return HttpResponseForbidden()

    parsed = urlparse(request.path)
    path = parsed.path
    response = HttpResponse()
    response['X-Accel-Redirect'] = settings.NGINX_PRIVATE_URL + path[len(settings.PRIVATE_MEDIA_URL):]
    return response
