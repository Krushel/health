from django.urls import path
from . import views
from .views import LandingView

urlpatterns = [
    path('health/', views.health_view, name='health'),
    path('', LandingView.as_view(), name='landing'),
]
