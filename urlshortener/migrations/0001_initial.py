# Generated by Django 4.1.7 on 2023-03-01 23:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import urlshortener.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_url', models.URLField()),
                ('short_url', models.CharField(default=urlshortener.models.generate_short_url, max_length=255, unique=True)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_clicked_date', models.DateTimeField(auto_now=True)),
                ('clicks_count', models.PositiveIntegerField(default=0)),
                ('link', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='clicks', to='urlshortener.link')),
            ],
        ),
    ]