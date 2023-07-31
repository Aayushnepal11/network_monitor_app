from django.contrib import admin
from .models import ServiceCatalog, CaptureURL
# Register your models here.
@admin.register(ServiceCatalog)
class ServiceManager(admin.ModelAdmin):
    list_display = ['title', 'description', 'image']
    list_per_page = 5

@admin.register(CaptureURL)
class URLManager(admin.ModelAdmin):
    list_display =  ["url_address_host", ]
    list_per_page = 7
