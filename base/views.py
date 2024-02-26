import os
from django.conf import settings
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .stt import stt
from .models import *
class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text"] = stt(File.objects.get().file)
        context["files"] = File.objects.all()
        return context

    