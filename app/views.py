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
    return JsonResponse({
        "result": "success",
        "message": "Success",
        "data": str(response),
        "version":"0.1"
    }, status=200)


from django.views.generic import TemplateView

class LandingView(TemplateView):
    template_name = "index.html"

def handler500(request):
    return JsonResponse({
        "result": "error",
        "message": "Unknown error",
        "data": "",
        "version":"0.1"

    }, status=500)

def handler404(request, exception):
    return JsonResponse({
        "result": "error",
        "message": "Page not found",
        "data": "",
        "version":"0.1"
    }, status=404)
    
def handler400(request, exception):
    return JsonResponse({
        "result": "error",
        "message": "Bad request",
        "data": "",
        "version":"0.1"
    }, status=400)

