from django.urls import path
from . import views, LandingView
from app import LandingView

urlpatterns = [
    path('health/', views.health_view),
    path('', LandingView.as_view()),
]
