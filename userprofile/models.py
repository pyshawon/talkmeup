from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    displayName = models.CharField(max_length=100, blank=True, default='')
    createdOn = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.displayName

    class Meta:
        ordering = ('-createdOn',)


class ContactedUserProfile(models.Model):
    contactName = models.CharField(max_length=100, blank=True, default='')
    contactEmail = models.CharField(max_length=100, blank=True, default='')
    contactPhone = models.CharField(max_length=100, blank=True, default='')
    contactMessage = models.CharField(max_length=1000, blank=True, default='')
    createdOn = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contactName

    class Meta:
        ordering = ('-createdOn',)
        
