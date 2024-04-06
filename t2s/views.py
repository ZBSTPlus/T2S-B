import os
from django.shortcuts import render
from pathlib import Path
from gtts import gTTS
from django.http import HttpResponse
def home(request):
    return render(request,'index.html')
def text_to_audio(request):
    if request.method == 'POST':
        text = request.POST.get('text', None)
        if text:
            language = "en"
            if any(char in "ఆ, ఈ, ఊ, ౠ, ౡ, ఏ, ఓ." for char in text):
                language = "te"  # Telugu
            elif any(char in "अ,आ,इ,ई,उ,ऊ,ऋ,ए,ऐ,ओ,औ" for char in text):
                language = "hi"  # Hindi
            
            tts = gTTS(text=text.strip(), lang=language)
            tts.save(Path(__file__).parent / "static/output.mp3")
        return render(request, 'text_to_audio.html',{"key":"ok",})
            # os.system("start output.mp3")
    return render(request, 'text_to_audio.html')


def about_us_view(request):
    return render(request, 'about_us.html')

# Create your views here.
