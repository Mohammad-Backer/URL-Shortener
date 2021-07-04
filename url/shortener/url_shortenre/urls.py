from django.urls import path
from . import views


app_name = 'url_shortenre'
urlpatterns = [
    path('', views.index, name='index'),
    path('short',views.shortened_url, name='short')
]

