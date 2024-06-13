from django.db import models
from django.template.defaultfilters import length

# Create your models{table} here.

class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)