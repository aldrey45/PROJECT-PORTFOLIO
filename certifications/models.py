from django.db import models

class Certification(models.Model):
    title = models.CharField(max_length=160)
    issuer = models.CharField(max_length=120)
    year = models.CharField(max_length=10, blank=True)
    credential_url = models.URLField(blank=True)
    badge_url = models.URLField(blank=True)

    class Meta:
        ordering = ["-year", "title"]

    def __str__(self) -> str:
        return self.title