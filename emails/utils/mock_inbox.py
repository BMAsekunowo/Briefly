import random
from datetime import datetime

MOCK_EMAILS = [
    ("team@briefly.ai", "Welcome to Briefly"),
    ("noreply@todo.com", "Your tasks for today"),
    ("accounts@service.com", "Billing Reminder"),
    ("offers@shop.com", "Today’s Discounts Inside!"),
    ("alerts@bank.com", "Unusual Activity Detected"),
]

def get_mock_emails(user_email):
    sample = random.sample(MOCK_EMAILS, k=3)
    timestamp = datetime.now().strftime("%H:%M:%S")
    return [{"from": sender, "subject": subject, "time": timestamp} for sender, subject in sample]