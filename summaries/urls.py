from django.urls import path
from . import views


urlpatterns = [
    path('my-summaries/', views.user_summaries, name='user_summaries'),
    path('my-summaries/<int:summary_id>/', views.summary_detail, name='summary_detail'),
    path("trigger-test/", views.trigger_test_summary, name="trigger-test-summary"),
]