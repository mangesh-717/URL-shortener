from django.db import models

# Create your models here.
# it is used to create table in postgress database 
class URL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=15, unique=True)
