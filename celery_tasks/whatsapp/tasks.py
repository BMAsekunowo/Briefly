from celery import shared_task
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()

@shared_task
def send_whatsapp_summary(user_id):
    try:
        user = User.objects.get(id=user_id)
        
        # Mock summary generation
        summary = f"""
        👋 Hello {user.username}!
        
        Here's your daily brief for {datetime.now().strftime('%A, %B %d, %Y')}:

        • 📧 You received 3 new emails today
        • ✅ 2 tasks were completed
        • 🔔 1 reminder is pending

        – Briefly 🧠
        """

        print(f"📤 WhatsApp Message to {user.username}:\n{summary}")

        return f"WhatsApp mock sent for user {user.username}"

    except User.DoesNotExist:
        print(f"❌ User with ID {user_id} not found.")
        return "User not found"