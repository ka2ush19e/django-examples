# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView, TemplateView
from core import urls as core_urls

urlpatterns = [
    # Core
    url(r'^', include(core_urls, namespace='core')),

    url(r'^favicon\.ico$', RedirectView.as_view(
        url=settings.STATIC_URL + 'images/favicon.ico', permanent=True), name='favicon.ico'),
    url(r'^robots\.txt$', TemplateView.as_view(
        template_name='robots.txt', content_type='text/plain'), name='robots.txt'),

    # Admin
    url(r'^admin/', admin.site.urls),

    # Application
]
