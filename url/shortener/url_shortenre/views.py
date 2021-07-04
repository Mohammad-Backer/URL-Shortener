from django.shortcuts import render
from pyshorteners import Shortener

from .models import url_strings 
import os


def shorten(url):
    
    Access_Token = os.environ.get('bitly_token')
    url_shortener = Shortener(api_key = Access_Token)
    shortened = url_shortener.bitly.short(url)
    return shortened

def index(request):
    
    return render(request, 'url_shortener/index.html')

def shortened_url(request):
    url_original = url_strings(url=request.POST['post-url'])
    url_original.url_short = shorten(url_original.url)
    url_original.url_title = request.POST['Title']
    url_original.save()
    short = url_original
    context = {"short":short}
    return render(request, 'url_shortener/index.html', context)

