# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.id, filename)

# Create your models here.
class CoachProfile(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to=user_directory_path)
    created_on = models.DateTimeField(auto_now_add=True)
    bio_text = models.TextField(max_length=3000)
    research_area = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    
    

    
