from __future__ import absolute_import
import os
from celery import Celery
print("CELERY FILE LOADED ✅")
# Set the default Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("Briefly")

# Load settings from Django settings, with `CELERY_` namespace
app.config_from_object("django.conf:settings", namespace="CELERY")

# Auto-discover tasks in all installed apps
app.autodiscover_tasks()

# ✅ Explicitly imported nested task modules so Celery can register them
@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    import emails.tasks.email_parse
    import celery_tasks.whatsapp.tasks


@app.task(bind=True)
def debug_task(self):
    print(f"✅ Hello from Celery! Request: {self.request!r}")