from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.health_view),
    path('', LandingView.as_view()),
]
