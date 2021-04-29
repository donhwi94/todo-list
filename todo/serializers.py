from rest_framework import serializers

from .models import Todo, Comment

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'is_completed', 'created_at', 'updated_at']

class CommentSerializer(serializers.ModelSerializer):
    todo = serializers.ReadOnlyField(source='todo.title')
    class Meta:
        model = Comment
        fields = ['id', 'todo', 'contents', 'created_at', 'updated_at']

class TodoDetailSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True)
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'is_completed', 'created_at', 'updated_at', 'comment_set']