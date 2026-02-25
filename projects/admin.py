from django.contrib import admin
from .models import Project, ProjectHighlight, ProjectSection


class HighlightInline(admin.TabularInline):
    model = ProjectHighlight
    extra = 1


class SectionInline(admin.TabularInline):
    model = ProjectSection
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "role", "year", "is_featured")
    list_filter = ("is_featured", "role", "year")
    search_fields = ("title", "slug", "one_liner")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [HighlightInline, SectionInline]
