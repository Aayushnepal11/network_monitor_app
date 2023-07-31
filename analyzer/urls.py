from django.urls import path
from .views import *

app_name = "nma_analyzer"
urlpatterns = [
    path('', AnalyzerPageView.as_view(),name='analyzer'),   
]
