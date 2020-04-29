from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    # Customize the admin panel to have these items displayed
    list_display = ('title', 'completed', 'created')

    # Add a search filter
    list_filter = ('title', 'completed', 'created')
# Register your models with the taskadmin.
admin.site.register(Task, TaskAdmin)