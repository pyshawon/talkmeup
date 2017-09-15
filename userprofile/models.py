from django.db import models


class UserProfile(models.Model):
    owner = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    displayName = models.CharField(max_length=100, blank=True, default='')
    createdOn = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.displayName

    class Meta:
        ordering = ('-createdOn',)
