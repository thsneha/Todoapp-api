from django.urls import path
from api import views
urlpatterns=[
    path("todos",views.TodosView.as_view()),
    path("todos/<int:todo_id>",views.TodoDetails.as_view()),
    path("users/accounts/signup",views.UserCreationView.as_view()),
    path("users/accounts/login",views.SignInView.as_view()),
]

#localhost:8000/api/v1/todos
