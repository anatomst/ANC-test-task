import random
import string

from django.db import models

from ANC_test_task.settings import SHORT_HOST


def generate_short_url():
    """
    Function to generate random symbol of 6 characters
    :return: example: "6NpxdR"
    """

    while True:
        short_url = ''.join(random.choice(string.ascii_letters + string.digits + "-") for _ in range(6))
        if not Link.objects.filter(short_url=short_url).exists():
            return SHORT_HOST + short_url


class Link(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=255, unique=True, default=generate_short_url)
    creator = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def get_symbol(self):
        return self.short_url.split("/")[-1]

    def __str__(self):
        return self.short_url


class Click(models.Model):
    link = models.OneToOneField(Link, on_delete=models.CASCADE, related_name="clicks")
    last_clicked_date = models.DateTimeField(auto_now=True)
    clicks_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.link.short_url}: {self.clicks_count}"
