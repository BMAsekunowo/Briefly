from django.db import models
from django.conf import settings


class Summary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Summary for {self.user.email} at {self.created_at}"


class EmailSummaryTrigger(models.Model):
    TRIGGER_CHOICES = [
        ("new_email", "New Email"),
        ("manual", "Manual"),
        ("scheduled", "Scheduled"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    triggered_at = models.DateTimeField(auto_now_add=True)
    trigger_type = models.CharField(max_length=20, choices=TRIGGER_CHOICES)
    triggered_by = models.CharField(max_length=50, default="system")

    def __str__(self):
        return f"{self.user.username} - {self.trigger_type} at {self.triggered_at}"