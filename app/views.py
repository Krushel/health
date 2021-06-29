from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
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

def too_many_requests(request, exception):
    return JsonResponse({
"result": "error",
"message": "Too many requests",
"params": {
request.content_params
},
"data": ""
}, status=429)

def handler500(request):
    return JsonResponse({
        "result": "error",
        "message": "Bad request",
        "params": {
            request.content_params
        },
        "data": ""
    }, status=500)

def handler404(request):
    return JsonResponse({
        "result": "error",
        "message": "Page not found",
        "params": {
            request.content_params
        },
        "data": ""
    }, status=500)
