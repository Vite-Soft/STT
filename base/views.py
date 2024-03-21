import os
from django.conf import settings
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .stt import stt
from .models import *
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

class HomeView(TemplateView):
    template_name = "pages/home.html"

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
    


@csrf_exempt
def upload_audio(request):
    if request.method == 'POST' and request.FILES.get('audio'):
        audio_file = request.FILES['audio']
        title = request.POST.get('title', 'Untitled')  # You can also get the title from the client-side
        audio_recording = File(file=audio_file)
        audio_recording.save()
        return JsonResponse({'message': 'Audio uploaded successfully.'})
    else:
        return JsonResponse({'error': 'No audio file found.'}, status=400)


