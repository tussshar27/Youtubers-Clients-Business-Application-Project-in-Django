from django.contrib import admin
from .models import Slider, Team
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):#class name can be anything
    
    def myphoto(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))


    list_display = ('id', 'myphoto', 'first_name', 'role', 'created_date') #display columns
    list_display_links = ('first_name','id')    #clickable column values
    search_fields = ('first_name', 'role')  #adds search feature based on the attributes mentioned.
    list_filter = ('role',) #, is required since list cannot have a single value and django has all in list format.

class SliderAdmin(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html('<img src="{}" width="200" />'.format(object.photo.url))

    list_display = ('id', 'headline', 'myphoto', 'button_text')
    list_display_links = ('headline',)


admin.site.register(Slider, SliderAdmin)
admin.site.register(Team, TeamAdmin)