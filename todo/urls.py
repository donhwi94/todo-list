from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from todo import views

urlpatterns = [
    path(r'todolist/', views.TodoList.as_view()),
    path(r'todolist/<int:pk>/', views.TodoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)