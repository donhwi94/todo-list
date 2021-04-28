from django.urls import path

from todo import views

urlpatterns = [
    path(r'todolist/', views.todo_list),
    path(r'todolist/<int:pk>/', views.todo_detail),
]