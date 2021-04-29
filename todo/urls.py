from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from todo import views

urlpatterns = [
    path(r'todolist/', views.todo_list),
    path(r'todolist/<int:pk>/', views.todo_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)