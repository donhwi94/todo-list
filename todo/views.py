from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse 
from rest_framework import renderers

from .models import Todo, Comment
from .serializers import TodoSerializer, CommentSerializer, TodoDetailSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'todolist' : reverse('todo-list', request=request, format=format)
    })

class TodoList(APIView):
    def get(self, request, format=None):
        todolist = Todo.objects.all().order_by('-created_at')
        serializer = TodoSerializer(todolist, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoDetail(APIView):
    def get_object(self, todo_id):
        try:
            return Todo.objects.get(pk=todo_id)
        except Todo.DoesNotExist:
            raise Http404

    def get(self, request, todo_id, format=None):
        todolist = self.get_object(todo_id)
        serializer = TodoDetailSerializer(todolist)
        return Response(serializer.data)

    def put(self, request, todo_id, format=None):
        todolist = self.get_object(todo_id)
        serializer = TodoSerializer(todolist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, todo_id, format=None):
        todolist = self.get_object(todo_id)
        todolist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CommentList(APIView):
    def get(self, request, todo_id, format=None):
        comments = Comment.objects.filter(todo_id=todo_id).order_by('-created_at')
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, todo_id, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(todo_id=todo_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetail(APIView):
    def get_object(self, comment_id):
        try:
            return Comment.objects.get(pk=comment_id)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, todo_id, comment_id, format=None):
        comments = self.get_object(comment_id)
        serializer = CommentSerializer(comments)
        return Response(serializer.data)

    def put(self, request, todo_id, comment_id, format=None):
        comments = self.get_object(comment_id)
        serializer = CommentSerializer(comments, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, todo_id, comment_id, format=None):
        comments = self.get_object(comment_id)
        comments.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)