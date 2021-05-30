from django.contrib import admin
from .models import Youtuber
from django.utils.html import format_html

class YtAdmin(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))



    list_display = ('id', 'name','myphoto', 'subs_count', 'category', 'is_featured')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'camera_type')
    list_filter = ('city', 'category')
    list_editable = ('is_featured',)

# Register your models here.
admin.site.register(Youtuber, YtAdmin)