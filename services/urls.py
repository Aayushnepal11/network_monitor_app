from django.urls import path
from .views import *

app_name = "nma_service"
urlpatterns = [
    path('', ServicePageView.as_view(),name='services'),
    path('ping/', PingView.as_view(),name='ping'),
    path('traceroute/', TraceRouteView.as_view(),name='traceroute'),
    path('passwordgenerator/', RandomPasswordView.as_view(),name='password_generator')
]






