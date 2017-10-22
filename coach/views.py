# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import CoachProfile

# Create your views here.
class IndexView(generic.ListView):
    template_name = "coach/index.html"
    context_object_name = 'coach_list'

    def get_queryset(self):
        return CoachProfile.objects.order_by('-created_on')

class DetailView(generic.DetailView):
    model = CoachProfile
    template_name = 'coach/detail.html'
    context_object_name = 'coach'
