from django.shortcuts import render, HttpResponse,redirect
from django.views.generic import FormView
from . forms import SearchForm
from .portscanner import simpleScan, read_binary
from django.contrib import messages
# Create your views here.


class ScannerPageView(FormView):
    template_name="scanner/scanner.html"
    form_class = SearchForm
    success_url = 'scanner/'


    def post(self, request, *args, **kwargs) :
        # post =  super().post(request, *args, **kwargs)
        global ip_address
        ip_address = request.POST.get('ip_address')
        simpleScan(ip_address)
        messages.success(request, "{}.pickle is saved file ".format(ip_address))
        return redirect('nma_scanner:scanner')

    
    def get_context_data(self, **kwargs):
        final_report = ['0.0.0.0', '1.1.1.1', '8.8.8.8',
                        '172.16.128.128', '192.168.1.1', '192.168.1.254']
        data = []
        for report in final_report:
            data.append(read_binary(report))
        context =  super().get_context_data(**kwargs)
        context['data'] = data
        context['ip_address'] = final_report
        return context