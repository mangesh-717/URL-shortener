# shortener/urls.py
from django.urls import path
from .views import shorten_url, redirect_original

urlpatterns = [
    path('', shorten_url, name='shorten_url'),
    path('short_code/', redirect_original, name='redirect_original'),
]
