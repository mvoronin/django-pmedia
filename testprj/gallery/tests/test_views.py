# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.test import TestCase
from django.test import Client
from gallery.models import Photo


class PrivateMediaTest(TestCase):
    fixtures = ["test/users.json", "test/photos.json"]

    def setUp(self):
        self.client = Client()

    def test_private_file(self):
        self.assertTrue(self.client.login(username='admin', password='django'))

        photo_obj = Photo.objects.get(pk=1)

        self.assertEqual(photo_obj.file.url, '/private/media/gallery/file1.jpg')

        expected_status_code = 200
        response = self.client.get(photo_obj.file.url)
        self.assertEqual(response.status_code, expected_status_code,
                         msg="Request '%(url)s'; response: %(returned_status_code)s != %(expected_status_code)s" % {
                             'url': photo_obj.file.url,
                             'returned_status_code': response.status_code,
                             'expected_status_code': expected_status_code})

        self.assertEqual(response['X-Accel-Redirect'], '/pmedia/gallery/file1.jpg')
