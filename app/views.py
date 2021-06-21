from django.shortcuts import render
from django.http import HttpResponse
from .tasks import add
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page

CACHE_TTL = 600


@cache_page(CACHE_TTL)
def health_view(request):
    response = add('heal','thy')
    return HttpResponse(response)
