from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from summaries.models import Summary
from django.contrib.auth import get_user_model


User = get_user_model()

@staff_member_required
def admin_dashboard(request):
    users = User.objects.all()
    summaries = Summary.objects.all().order_by('-created_at')[:10]
    return render(request, 'dashboard.html', {
        'users': users,
        'summaries': summaries
})