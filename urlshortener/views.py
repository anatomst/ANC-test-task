from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Link

from .serializers import LinkSerializer


class LinkCreateView(APIView):
    def post(self, request):
        long_url = request.data.get('long_url', '')
        existing_link = Link.objects.filter(long_url=long_url).first()
        if existing_link:
            return JsonResponse({"info": f"This URL has already short link - {existing_link.short_url}"}, status=400)
        serializer = LinkSerializer(data=request.data)
        if serializer.is_valid():
            if request.user.is_authenticated:
                serializer.save(creator=request.user)
            else:
                ip_address = request.META.get('HTTP_X_FORWARDED_FOR', None)
                if ip_address is None:
                    ip_address = request.META.get('REMOTE_ADDR')
                serializer.save(ip_address=ip_address)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)