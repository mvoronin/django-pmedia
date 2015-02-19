from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models


class Photo(models.Model):
    file = models.ImageField(upload_to='gallery',
                             storage=FileSystemStorage(location=settings.PRIVATE_MEDIA_ROOT,
                                                       base_url=settings.PRIVATE_MEDIA_URL))
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        permissions = (
            ("view_private_files", "Can view private files"),
        )
