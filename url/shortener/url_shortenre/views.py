from django.utils import timezone
from django.urls import reverse
from django.views import generic 
from django.http import HttpResponseRedirect

from pyshorteners import Shortener

import validators 

from .models import url_strings 
import os




def shorten(url):
    
    Access_Token = os.environ.get('bitly_token').strip("'")
    url_shortener = Shortener(api_key = Access_Token)
    shortened = url_shortener.bitly.short(url)
    return shortened

class IndexView(generic.ListView):
    template_name = 'url_shortener/index.html'
    model = url_strings
    context_object_name = 'short'

    def get_queryset(self):
        return url_strings.objects.filter(
            pub_date__lte = timezone.now()
        ).order_by('-pub_date')[:5]


def shortened_url(request):

    posted_url = request.POST['post-url']
    if validators.url(posted_url):
        url_original = url_strings(url=posted_url)
        url_original.url_short = shorten(url_original.url)
        url_original.url_title = request.POST['Title']
        url_original.pub_date = timezone.now()
        url_original.save()
    return HttpResponseRedirect(reverse('url_shortenre:index'))

