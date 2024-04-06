from django.urls import path
#from .views import home
from .views import text_to_audio ,home,about_us_view

urlpatterns = [
    path('', home, name='home'),
    path('text-to-audio/', text_to_audio, name='text_to_audio'),
    path('about-us/', about_us_view, name='about_us'),
]