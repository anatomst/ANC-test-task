import random
import string

from django.db import models
from django.contrib.auth.models import User


class Link(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=6, unique=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ip_address = models.GenericIPAddressField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)
    clicks = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.short_url

    # def save(self, *args, **kwargs):
    #     request = kwargs.pop('request', None)
    #     if not self.pk:
    #         if request is not None and not request.user.is_authenticated:
    #             self.ip_address = request.META.get('REMOTE_ADDR')
    #     super().save(*args, **kwargs)
# Link.objects.create(long_url="http://127.0.0.1:8000/iaudgcshbiaus")