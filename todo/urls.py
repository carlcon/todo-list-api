from django.urls import path
from todo import views

urlpatterns = [
    path('todos/', views.TodoList.as_view()),
    path('todos/<int:pk>', views.TodoDetail.as_view())
]