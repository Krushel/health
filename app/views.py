from django.shortcuts import render
from django.http import HttpResponse
from .tasks import add

def health_view(request):
    response = add('heal','thy')
    return HttpResponse(response)
