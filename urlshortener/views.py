from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import JsonResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from rest_framework.response import Response
from rest_framework.views import APIView

from ANC_test_task.settings import SHORT_HOST
from .forms import LinkForm
from .models import Link, Click

from .serializers import LinkSerializer


class LinkCreateViewAPI(APIView):
    """
    API View to create short URL.
    request example: {"long_url": "https://example.com/en/stable/userguide/periodic-tasks1.html"}
    response example:
    {
        "long_url": "https://example.com/en/stable/userguide/periodic-tasks1.html",
        "short_url": "http://127.0.0.1:8000/redirect/gUz2-i"
    }
    """

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
                ip_address = request.META.get('REMOTE_ADDR')
                serializer.save(ip_address=ip_address)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class LinkCreateViewUsingAPI(generic.View):
    """
    View to create a short URL using API.
    """
    template_name = 'create_using_api.html'

    def get(self, request):
        return render(request, self.template_name)


class LinkCreateView(generic.CreateView):
    """
    Django view to create short URL in browser
    """

    template_name = "create_short_url.html"
    form_class = LinkForm

    def form_valid(self, form):
        existing_link = Link.objects.filter(long_url=form.cleaned_data["long_url"]).first()
        if existing_link:
            return render(self.request, template_name='link_consists.html', context={"link": existing_link})

        if self.request.user.is_authenticated:
            form.instance.creator = self.request.user
        else:
            form.instance.ip_address = self.request.META.get('REMOTE_ADDR')
        try:
            return super().form_valid(form)
        except ValidationError as e:
            messages.error(self.request, e.message)
            return self.form_invalid(form)

    def get_success_url(self):
        Click.objects.create(link=self.object)
        return reverse_lazy("urlshortener:link_detail", kwargs={'symbol': self.object.get_symbol()})


class LinkStatsView(generic.DetailView):
    """
    Django view to get detail info about short link (clicks, last click).
    Only creator can get this information
    """

    model = Link
    template_name = 'link_detail.html'

    def get_object(self, queryset=None):
        symbol = self.kwargs.get('symbol')
        short_url = SHORT_HOST + symbol
        return get_object_or_404(Link, short_url=short_url, is_deleted=False)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.creator == request.user or self.object.ip_address == request.META.get('REMOTE_ADDR'):
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        raise Http404("You are not authorized to view this page")


class LinkDeleteConfirmView(generic.TemplateView):
    """
    Confirmation page
    """

    template_name = 'link_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        symbol = self.kwargs.get('symbol')
        short_url = SHORT_HOST + symbol
        context['object'] = get_object_or_404(Link, short_url=short_url)
        return context


class LinkDeleteView(generic.View):
    """
    Django view to "delete" link from DB.
    It's only change status of is_deleted to True
    """

    success_url = reverse_lazy('urlshortener:shortner')

    def post(self, request, symbol):

        short_url = SHORT_HOST + symbol
        obj = get_object_or_404(Link, short_url=short_url)
        if obj.creator == request.user or obj.ip_address == request.META.get('REMOTE_ADDR'):
            obj.is_deleted = True
            obj.save()
            return HttpResponseRedirect(self.success_url)
        raise Http404("You are not authorized to delete this link")


class LinkRedirectView(generic.RedirectView):
    """
    Django view to redirect from short link to original link
    """

    def get_redirect_url(self, *args, **kwargs):
        short_url = SHORT_HOST + kwargs.get('symbol')
        link = get_object_or_404(Link, short_url=short_url)
        try:
            click = Click.objects.get(link=link)
        except Click.DoesNotExist:
            click = Click.objects.create(link=link)
        click.clicks_count += 1
        click.save()
        return link.long_url
