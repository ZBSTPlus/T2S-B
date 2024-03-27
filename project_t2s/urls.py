from django.contrib import admin
from django.urls import path, include
#from .t2s.views import text_to_audio ,home
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',include('t2s.urls')),
    path('admin/',admin.site.urls)
    #path('', home, name='home'),
    #path('text-to-audio/', text_to_audio, name='text_to_audio'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
