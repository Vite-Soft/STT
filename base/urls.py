from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('upload-audio/', upload_audio, name='upload_audio'),
]
