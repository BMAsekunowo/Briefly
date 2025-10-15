from django.contrib import admin
from django.urls import path
from visual.views import homePage
from dashboard.views import admin_dashboard
from django.urls import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('visual.urls')),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('', include('summaries.urls')),
    path('', include('users.urls')),
]
