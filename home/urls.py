from django.urls import path
from . views import *
app_name = 'nma_home'

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
]