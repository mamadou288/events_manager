from django.contrib import admin
from .models import Event 


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'creator', 'start_time', 'end_time', 'event_type', 'visibility')
    search_fields = ('id','title', 'description', 'location')
    list_filter = ('event_type', 'visibility', 'start_time')