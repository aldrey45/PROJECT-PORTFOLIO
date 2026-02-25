from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=120)
    headline = models.CharField(max_length=180, blank=True)
    tagline = models.CharField(max_length=240, blank=True)
    location = models.CharField(max_length=120, blank=True)
    email = models.EmailField(blank=True)

    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    resume_url = models.URLField(blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class SnapshotItem(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="snapshots")
    title = models.CharField(max_length=80)
    subtitle = models.CharField(max_length=140, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self) -> str:
        return self.title