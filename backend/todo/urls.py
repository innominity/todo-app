from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.get_tasks),
    path('task/create/', views.create_task),
    path('task/remove/', views.remove_task),
    path('task/update-status/<int:task_id>/', views.update_task_status),
]
