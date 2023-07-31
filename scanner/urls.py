from django.urls import path
from .views import *

app_name = "nma_scanner"
urlpatterns = [
    path('', ScannerPageView.as_view(),name='scanner'),   
]
