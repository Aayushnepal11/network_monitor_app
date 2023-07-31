from django.shortcuts import HttpResponse,render
from django.views.generic import TemplateView
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


plt.switch_backend("Agg")


class HomePageView(TemplateView):
    template_name='home/index.html'

    def get_context_data(self, **kwargs):
        labels = ["Cisco", "Arista", "Juniper"]
        sizes = [60, 15, 25]
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, explode=(0,0.1,0),
                colors=["#BCCCE0", "red", "green"],
                autopct='%1.1f%%', shadow=True, startangle=90, 
                textprops={'color': '#fff', 'fontsize': 15})
        
        def figure_path(figure_name):
            return "static/chart/{}".format(figure_name)
        
        fig_path = figure_path("pie.png")
        fig.savefig(fig_path, transparent=True)

        fig, ax = plt.subplots()
        fig.set_alpha(.5)
        ax.set_xlabel("Network Performance")
        ax.set_ylabel("Network Availability")
        x = np.arange(0, 2*np.pi, 0.01)
        line, = ax.plot(x, np.sin(x))

        def animate(i):
            line.set_ydata(np.sin(x + i / 50))
            return line,

        ani = animation.FuncAnimation(
            fig, animate, interval=20, blit=True, save_count=50,repeat=True,
        )
        writer = animation.FFMpegWriter(
        fps=15, metadata=dict(artist='Me'), bitrate=1800)
        
        ani_path = figure_path('loop_network.mp4')
        ani.save(ani_path, writer=writer)


        context =  super().get_context_data(**kwargs)     
        context["figure_path", ani_path] = fig_path, ani_path

        return context


