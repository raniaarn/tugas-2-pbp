from django.urls import path
from todolist.views import register, login_user, logout_user, show_todolist, create_task, delete_task, edit_task


app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('delete-task/<str:pk>/', delete_task, name='delete_task'),
    path('edit-task/<str:pk>/', edit_task, name='edit_task'),
]