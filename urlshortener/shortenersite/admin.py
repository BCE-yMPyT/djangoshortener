from django.contrib import admin
from shortenersite.models import Urls
# Register your models here.

class UrlsAdmin(admin.ModelAdmin):
    list_display = ('short_id','httpurl','pub_date', 'count', 'text')
    ordering = ('-pub_date',)

admin.site.register(Urls, UrlsAdmin) # Register the Urls model with UrlsAdmin options
