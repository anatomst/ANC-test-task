from rest_framework import serializers
from .models import Link, Click


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('long_url', 'short_url')
        read_only_fields = ('id', 'short_url', 'creator', 'ip_address', 'created_at', 'deleted')

    def create(self, validated_data):
        link = Link.objects.create(**validated_data)
        Click.objects.create(link=link)
        return link
