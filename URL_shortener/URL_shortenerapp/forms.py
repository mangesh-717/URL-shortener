# shortener/forms.py
from django import forms
from .models import URL

# it is udesd to create form with thehelp of django 
class URLForm(forms.ModelForm):
    class Meta:
        model = URL
        fields = ['original_url']
         
