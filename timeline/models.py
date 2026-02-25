from django.db import models

class TimelineItem(models.Model):
    TYPE_CHOICES = [
        ("school", "School"),
        ("ojt", "OJT"),
        ("capstone", "Capstone"),
        ("cert", "Certification"),
        ("project", "Project"),
    ]

    title = models.CharField(max_length=120)
    date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default="school")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "-date", "-id"]

    def __str__(self) -> str:
        return self.title