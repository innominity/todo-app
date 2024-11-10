from django.db import models


class TodoTask(models.Model):

    class TodoTaskStatus(models.IntegerChoices):
        ACTIVE = 1  # Активная
        DONE = 2    # Выполнена

    title = models.CharField(max_length=500) # Наименование задания
    created_at = models.DateTimeField(auto_now_add=True) # Дата создания
    status = models.IntegerField(choices=TodoTaskStatus.choices, default=TodoTaskStatus.ACTIVE) # Статус задачи

    class Meta:

        verbose_name = 'TODO задача'
        verbose_name_plural = 'TODO задачи'
        ordering = ['-created_at']