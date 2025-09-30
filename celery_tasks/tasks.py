from celery import shared_task

@shared_task
def test_celery_task():
    print("✅ Celery task executed successfully.")
    return "This is a response from your first Celery task"

@shared_task
def scheduled_hello():
    print("👋 This task runs on a schedule via Celery Beat.")