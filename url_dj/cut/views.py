from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin

from cut.forms import UrlsForm
from cut.models import Url
from cut.utils import to_short_url


class UrlCreateView(CreateView):
    """
    View for takiun user url, converting into short and save into DB.
    """

    model = Url
    form_class = UrlsForm
    template_name = "cut/index.html"

    def post(self, request):
        form = UrlsForm(request.POST)
        try:
            short_url = to_short_url(request.POST.get("user_url"))
        except TypeError:
            return HttpResponseRedirect(reverse_lazy("error"))
        if form.is_valid():
            url = form.save(commit=False)
            url.short_url = settings.HOST_URL + "/" + short_url
            url.user = request.user
            url.save()
            return HttpResponseRedirect(reverse_lazy("detail", args=[url.id]))
        return render(request, "cut/index.html", {"form": form})


class UrlListView(LoginRequiredMixin, ListView):
    model = Url
    template_name = "cut/list.html"
    context_object_name = "urls"

    def get_queryset(self):
        return Url.objects.filter(user=self.request.user)


def get_url(request, id):
    """
    DetailView created by function.
    """
    urls = Url.objects.get(id=id)
    return render(request, "cut/short_url.html", context={"urls": urls})


def error_page(request):
    return render(request, "cut/error.html")
