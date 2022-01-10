from django.shortcuts import render
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.conf import settings

from cut.forms import UrlsForm
from cut.models import Url
from cut.utils import to_short_url


class UrlCreateView(CreateView):
    model = Url
    form_class = UrlsForm
    template_name = "cut/index.html"

    def post(self, request):
        form = UrlsForm(request.POST)
        sat = to_short_url(request.POST.get("user_url"))
        short_url = sat
        if form.is_valid():
            url = form.save(commit=False)
            url.short_url = settings.HOST_URL + '/' + short_url
            url.save()
            return HttpResponseRedirect(reverse_lazy("detail", args=[url.id]))
        return render(request, "cut/index.html", {"form": form})


def get_url(request, id):
    urls = Url.objects.get(id=id)
    return render(request, "cut/short_url.html", context={"urls": urls})
