from celery import shared_task
from django.contrib.auth import get_user_model
from emails.services.parsing_service import parse_user_inbox
from summaries.models import Summary

User = get_user_model()

@shared_task
def parse_user_emails(user_id):
    try:
        user = User.objects.get(id=user_id)
        parsed_emails = parse_user_inbox(user)

        # ✅ Save to Summaries BEFORE returning
        summary_content = f"Parsed {len(parsed_emails)} emails for {user.username}."
        Summary.objects.create(user=user, content=summary_content)
        print(f"✅ Summary created for {user.username}.")

        return f"Email parsing and summary creation simulated for {user.username} ({len(parsed_emails)} emails)"
    
    except User.DoesNotExist:
        print(f"❌ User with ID {user_id} not found.")
        return "User not found"