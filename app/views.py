from django.shortcuts import render
from django.http import HttpResponse
from .tasks import add
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView

CACHE_TTL = 60 * 10 #10 minutes


@cache_page(CACHE_TTL)
def health_view(request):
    response = add('heal','thy')
    return HttpResponse(response)

from django.views.generic import TemplateView

class LandingView(TemplateView):
    template_name = "index.html"
    
