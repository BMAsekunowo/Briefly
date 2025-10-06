from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from celery_tasks.whatsapp.tasks import send_whatsapp_summary

User = get_user_model()

class Command(BaseCommand):
    help = "Trigger WhatsApp summary task for all active users."

    def handle(self, *args, **kwargs):
        active_users = User.objects.filter(is_active=True)
        for user in active_users:
            send_whatsapp_summary.delay(user.id)
            self.stdout.write(self.style.SUCCESS(f"Queued summary task for {user.username}"))