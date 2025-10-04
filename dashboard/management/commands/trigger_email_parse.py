from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from emails.tasks.email_parse import parse_user_emails

User = get_user_model()

class Command(BaseCommand):
    help = "Trigger mock email parsing task for all active users."

    def handle(self, *args, **kwargs):
        active_users = User.objects.filter(is_active=True)
        for user in active_users:
            parse_user_emails.delay(user.id)
            self.stdout.write(self.style.SUCCESS(f"📥 Queued email parsing for {user.username}"))