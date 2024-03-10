from django.contrib import admin
from django.urls import path, include
#from .t2s.views import text_to_audio ,home


urlpatterns = [
    path('',include('t2s.urls')),
    path('admin/',admin.site.urls)
    #path('', home, name='home'),
    #path('text-to-audio/', text_to_audio, name='text_to_audio'),
]