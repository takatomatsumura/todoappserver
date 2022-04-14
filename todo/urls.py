from django.urls import path
from todo import views


urlpatterns = [
    path("todolist/1/<str:uuid>", views.todolisttrue),
    path("todolist/0/<str:uuid>", views.todolistfalse),
    path("todolist/len/<str:uuid>", views.opacitylen),
    path("retrieve/<str:pk>", views.TodoRetrieveView.as_view()),
    path("create", views.todocreate),
    path("donebool/<str:pk>", views.TodoUpdateView.as_view()),
    path("update/<str:pk>", views.todoupdate),
    path("delete/<str:pk>", views.TodoDeleteView.as_view()),
    path("user/list", views.UserList.as_view()),
    path("user/retrieve/<str:uuid>", views.userretrieve),
    path("user/create", views.UserCreate.as_view()),
    path("user/update/<str:pk>", views.UserUpdate.as_view()),
    path("notificationtarget/<str:uuid>", views.notificationtarget),
    path("notification/overdue/<str:uuid>", views.notificationlength),
]
