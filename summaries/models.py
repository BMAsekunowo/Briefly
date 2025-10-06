from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Summary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='summaries')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return f"Summary for {self.user.username} on {self.created_at.strftime('%Y-%m-%d %H:%M')}"