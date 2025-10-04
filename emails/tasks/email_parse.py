from celery import shared_task
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()

@shared_task
def parse_user_emails(user_id):
    try:
        user = User.objects.get(id=user_id)

        # Simulated email parsing logic
        parsed_emails = [
            {"subject": "Welcome to Briefly", "from": "team@briefly.ai"},
            {"subject": "Your tasks for today", "from": "noreply@todo.com"},
            {"subject": "Billing Reminder", "from": "accounts@service.com"},
        ]

        print(f"📨 Parsed {len(parsed_emails)} emails for {user.username} at {datetime.now().strftime('%H:%M:%S')}")

        for email in parsed_emails:
            print(f"   - {email['subject']} from {email['from']}")

        return f"Email parsing simulated for {user.username}"

    except User.DoesNotExist:
        print(f"❌ User with ID {user_id} not found.")
        return "User not found"