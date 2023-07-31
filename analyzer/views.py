from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
# Create your views here.


class AnalyzerPageView(TemplateView):
    
    def get(self, request):
        return HttpResponse("Analyzer Page")
