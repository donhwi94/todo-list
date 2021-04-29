from django.urls import path

from todo import views

urlpatterns = [
    path('', views.api_root),
    path('todos/', views.TodoList.as_view(), name='todo-list'),
    path('todos/<int:todo_id>/', views.TodoDetail.as_view(), name='todo-detail'),
    path('todos/<int:todo_id>/comments/', views.CommentList.as_view(), name='comment-list'),
    path('todos/<int:todo_id>/comments/<int:comment_id>/', views.CommentDetail.as_view(), name='comment-detail'),
]