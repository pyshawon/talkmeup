# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CoachProfile(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='coach_photos/%Y/%m/%d')
    created_on = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, default='')
    affiliation = models.CharField(max_length=100, default='')
    secondary_affiliation = models.CharField(max_length=100, default='')
    bio_text = models.TextField(max_length=3000, default='')
    research_area = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.name
    
    

    
