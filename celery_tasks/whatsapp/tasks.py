from celery import shared_task
from django.contrib.auth import get_user_model
from summaries.models import Summary

User = get_user_model()

@shared_task
def send_whatsapp_summary(user_id):
    try:
        user = User.objects.get(id=user_id)

        # 🧠 Fetch the latest summary created for the user
        summary = Summary.objects.filter(user=user).order_by('-created_at').first()

        if summary:
            # Simulate sending the summary content via WhatsApp
            print(f"📤 WhatsApp Summary to {user.username}:\n{summary.content}")

            # Mark the summary as delivered
            summary.delivered = True
            summary.save()

            return f"✅ WhatsApp summary sent and marked delivered for {user.username}"

        else:
            print(f"⚠️ No summary found for {user.username}")
            return "No summary to send"

    except User.DoesNotExist:
        print(f"❌ User with ID {user_id} not found.")
        return "User not found"