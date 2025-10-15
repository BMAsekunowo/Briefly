from celery import shared_task
from django.contrib.auth import get_user_model
from summaries.models import Summary, EmailSummaryTrigger

User = get_user_model()

@shared_task
def generate_summary_from_email(user_id, email_subject, email_body):
    try:
        user = User.objects.get(id=user_id)
        content = f"📥 New Email Summary:\nSubject: {email_subject}\n\n{email_body}"

        Summary.objects.create(user=user, content=content)
        EmailSummaryTrigger.objects.create(
            user=user,
            trigger_type="new_email",
            triggered_by="system"
        )
        return f"Summary generated for {user.email}"

    except User.DoesNotExist:
        return "User not found"