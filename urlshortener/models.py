import random
import string

from django.db import models


def generate_short_symbol():
    while True:
        symbol = ''.join(random.choice(string.ascii_letters + string.digits + "-") for _ in range(6))
        if not Link.objects.filter(short_symbol=symbol).exists():
            return symbol


class Link(models.Model):
    long_url = models.URLField()
    short_symbol = models.CharField(max_length=6, unique=True, default=generate_short_symbol)
    creator = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    def short_url(self):
        return f"http://127.0.0.1:8000/redirect/{self.short_symbol}"

    def __str__(self):
        return self.short_url


class Click(models.Model):
    link = models.OneToOneField(Link, on_delete=models.CASCADE, related_name="clicks")
    last_clicked_date = models.DateTimeField(auto_now=True)
    clicks_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.link.short_url}: {self.clicks_count}"
