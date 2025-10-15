from django.contrib import admin
from .models import Summary, EmailSummaryTrigger

@admin.register(Summary)
class SummaryAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'created_at')  
    list_filter = ('created_at',) 

@admin.register(EmailSummaryTrigger)
class EmailSummaryTriggerAdmin(admin.ModelAdmin):
    list_display = ('user', 'trigger_type', 'triggered_at', 'triggered_by')
    list_filter = ('trigger_type',)