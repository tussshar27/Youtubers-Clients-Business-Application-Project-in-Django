from django.contrib import admin
from .models import Hiretuber, Contacttuber
from django.utils.html import format_html

# Register your models here.
class HtAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'email', 'tuber_name')
    list_display_links = ('first_name', )
    search_fields = ('first_name', 'tuber_name')
    list_filter = ('tuber_name',)

class CtAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'ph_number', 'email')
    list_display_links = ('full_name', )

admin.site.register(Hiretuber, HtAdmin)
admin.site.register(Contacttuber, CtAdmin)