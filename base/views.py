import os
from django.conf import settings
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .stt import stt
from .models import *

class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = "data"
        return context
    

class FileListView(TemplateView):
    template_name = "pages/file.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = []
        for i in File.objects.all():
            temp = {
                'url': i.file.url,
                'text': stt(i.file)
            }
            data.append(temp)
        context['data'] = data
        return context