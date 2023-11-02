from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.registration, name='registration'),
    path('login', views.login, name = 'login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('task-detail', views.task_detail, name='task_detail'),
    path('todoapp', views.todo_list, name='todo_list'),
    path('logout', views.logout, name = 'logout'),
    path('post/<str:user>', views.post, name = 'post'),
    # Add more URL patterns here
    
]
