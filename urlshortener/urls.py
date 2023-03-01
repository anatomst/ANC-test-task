from django.urls import path

from urlshortener.views import LinkCreateViewAPI, LinkCreateView, LinkStatsView, LinkRedirectView, LinkDeleteView, \
    LinkDeleteConfirmView

urlpatterns = [
    path("api/shortner/", LinkCreateViewAPI.as_view(), name="create_short_url_api"),
    path('shortner/', LinkCreateView.as_view(), name='shortner'),
    path('shortner/<str:symbol>/stats/', LinkStatsView.as_view(), name='link_detail'),
    path('shortner/<str:symbol>/confirm/', LinkDeleteConfirmView.as_view(), name='link_confirm'),
    path('shortner/<str:symbol>/delete/', LinkDeleteView.as_view(), name='link_delete'),
    path('redirect/<str:symbol>/', LinkRedirectView.as_view(), name='redirect'),
]

app_name = "urlshortener"
