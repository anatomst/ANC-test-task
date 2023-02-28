import random
import string

from django.db import models


class Link(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=6, unique=True)
    creator = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)
    clicks = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = self.generate_short_url()
        super().save(*args, **kwargs)

    @staticmethod
    def generate_short_url():
        while True:
            short_url = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
            if not Link.objects.filter(short_url=short_url).exists():
                return f"http://127.0.0.1:8000/redirect/{short_url}"

    def __str__(self):
        return self.short_url
