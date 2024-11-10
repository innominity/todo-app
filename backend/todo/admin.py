from django.contrib import admin
from .models import TodoTask

class TodoTaskAdmin(admin.ModelAdmin):

    class Meta:
        list_display = ['id', 'title', 'created_at', 'status']
        list_display_links = ['id', 'title']


admin.site.register(TodoTask, TodoTaskAdmin)