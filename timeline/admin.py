from django.contrib import admin
from .models import TimelineItem


@admin.register(TimelineItem)
class TimelineAdmin(admin.ModelAdmin):
    list_display = ("title", "type", "date", "order")
    list_filter = ("type",)
    ordering = ("order", "-date")
