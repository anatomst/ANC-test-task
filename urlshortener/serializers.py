from rest_framework import serializers
from .models import Link


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('id', 'long_url', 'short_url', 'creator', 'ip_address', 'created_at', 'deleted', 'clicks')
        read_only_fields = ('id', 'short_url', 'creator', 'ip_address', 'created_at', 'deleted', 'clicks')
