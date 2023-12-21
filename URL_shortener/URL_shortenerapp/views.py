# shortener/views.py
from django.shortcuts import render, redirect
from .models import URL
from .forms import URLForm
import random
import string
def generate_short_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(6))

 
def shorten_url(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['original_url']
            short_code = generate_short_code()
            URL.objects.create(original_url=url, short_code=short_code)
            return render(request, 'success.html', {'short_url': url+short_code})
    else:
        form = URLForm()
    return render(request, 'index.html', {'form': form})


def redirect_original(request, short_code):
    url = URL.objects.get(short_code=short_code)
    return redirect(url.original_url)


