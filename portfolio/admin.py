from django.contrib import admin
from .models import Profile, SnapshotItem


class SnapshotInline(admin.TabularInline):
    model = SnapshotItem
    extra = 1


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "headline", "location", "updated_at")
    inlines = [SnapshotInline]
