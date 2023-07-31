from typing import Iterable, Optional
from django.db import models

# Create your models here.

class ServiceCatalog(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    image = models.ImageField(upload_to="uploads/")
    url = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural="Service Catalog"
    
    
    def __str__(self):
        return self.title


class CaptureURL(models.Model):
    url_address_host = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural= "URL Address"

    def __str__(self):
        return self.url_address_host
    