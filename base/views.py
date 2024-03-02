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
    

class FileListView(ListView):
    model = File
    template_name = "pages/file.html"
    paginate_by = 100  # if pagination is desired
    
    def get_context_data(self, **kwargs):
        # TEXT = (1,)
        context = super().get_context_data(**kwargs)
        for i in File.objects.all():
        #    TEXT = TEXT + (stt(i.file),)
            context["text"] = stt(i.file)
            return context
        # context["text"] = stt(i.file)
        # return context