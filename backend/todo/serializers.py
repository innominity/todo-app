from rest_framework import serializers
from .models import TodoTask

class TodoTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoTask
        fields = (
            'id',
            'title',
            'created_at',
            'status'
        )