from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Summary
from celery_tasks.tasks import generate_summary_from_email  

@login_required
def user_summaries(request):
    summaries = Summary.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'my_summaries.html', {
        'summaries': summaries
})
    
@login_required
def summary_detail(request, summary_id):
    summary = get_object_or_404(Summary, id=summary_id, user=request.user)
    return render(request, 'summaries/summary_detail.html', {
        'summary': summary
})
    
@login_required
def trigger_test_summary(request):
    subject = "Test Subject"
    body = "This is a simulated email body for parsing."
    generate_summary_from_email.delay(request.user.id, subject, body)
    return redirect("home")