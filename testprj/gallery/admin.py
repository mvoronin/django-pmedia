# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from gallery.models import Photo


class PhotoAdmin(ModelAdmin):
    pass

admin.site.register(Photo, PhotoAdmin)
