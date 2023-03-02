from django.contrib import admin

from urlshortener.models import Link, Click

admin.site.register(Link)
admin.site.register(Click)
