from django.urls import path
from todolist.views import add_task, delete, login_user, register, logout_user, show_todolist, create_task, change_task_status, delete_task, todolist_json
app_name = "todolist"

urlpatterns = [
    path("", show_todolist, name = "show_todolist"),
    path("register/", register, name = "register"),
    path("login/", login_user, name = "login"),
    path("logout/", logout_user, name = "logout"),
    path("create-task/", create_task, name = "create-task"),
    path("change-task-status/<int:pk>/", change_task_status, name = "change-task-status"),
    path("delete-task/<int:pk>/", delete_task, name = "delete-task"),
    path('json/', todolist_json, name = "json"),
    path('add/', add_task, name = 'add-task'),
    path('delete/<int:pk>/', delete, name = 'delete'),
] 