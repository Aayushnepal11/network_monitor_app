from django.shortcuts import render, HttpResponse
from django.views.generic import *
from .models import ServiceCatalog, CaptureURL
import ping3
from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sr
import threading


# Create your views here.
class ServicePageView(TemplateView):
    template_name = "services/services.html"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)

        context['services'] = ServiceCatalog.objects.all()

        return context


class PingView(ListView):
    template_name ="services/ping.html"
    model=CaptureURL


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        responses=dict()
        for urls in self.model.objects.all():
            responses[urls]=ping3.ping(str(urls))
        context["response_time"] = responses
        return context

    

class TraceRouteView(DetailView):
    template_name = "services/traceroute.html"
    model=CaptureURL

    def get(self, request):
        target_host = "example.com"
        responses = self.perform_traceroute(target_host)
        context = {
            'target_host': self.model.objects.all(),
            'results': responses,
        }
        return render(request, self.template_name, context)
    
    def perform_traceroute(self, target_host, max_hops=30):
        results = []
        threads = []

        def traceroute_worker(ttl):
            packet = IP(dst=target_host, ttl=ttl) / ICMP()
            reply, _ = sr(packet, verbose=False, timeout=2)

            if reply:
                results.append(reply[0][1].src)
            else:
                results.append('*')

            if reply and reply[0][1].type == 0:
                return True
            return False

        for ttl in range(1, max_hops + 1):
            thread = threading.Thread(target=traceroute_worker, args=(ttl,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        return results
