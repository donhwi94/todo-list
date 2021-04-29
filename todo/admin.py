from django.contrib import admin

from .models import Todo
from .models import Comment

admin.site.register(Todo)
admin.site.register(Comment)