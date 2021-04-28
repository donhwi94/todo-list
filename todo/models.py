from django.db import models

class Todo(models.Model):
    # id = models.AutoField() # 자동 생성
    title = models.TextField(blank=False)
    description = models.TextField(blank=False)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

class Comment(models.Model):
    # id = models.AutoField() # 자동 생성
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    contents = models.TextField(blank=False)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    