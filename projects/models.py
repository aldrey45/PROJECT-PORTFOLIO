from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=160)
    slug = models.SlugField(max_length=180, unique=True)
    one_liner = models.CharField(max_length=220)
    overview = models.TextField(blank=True)

    role = models.CharField(max_length=60)
    year = models.CharField(max_length=9, blank=True)
    is_featured = models.BooleanField(default=False)

    tech_stack = models.JSONField(default=list, blank=True)
    tags = models.JSONField(default=list, blank=True)

    repo_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-is_featured", "-created_at", "title"]

    def __str__(self) -> str:
        return self.title


class ProjectHighlight(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="highlights")
    text = models.CharField(max_length=220)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self) -> str:
        return self.text


class ProjectSection(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="sections")
    title = models.CharField(max_length=80)
    content = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self) -> str:
        return f"{self.project.slug}: {self.title}"