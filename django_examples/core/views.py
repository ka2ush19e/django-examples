# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals
from django.views.generic import TemplateView


class HomeListView(TemplateView):
    template_name = 'core/home.html'
