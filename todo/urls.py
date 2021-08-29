from django.urls import path
from todo import views


urlpatterns = [
     path("list/len", views.listlength),
     path("list/0", views.ListViewBoolFalse.as_view()),
     path("list/1", views.ListViewBoolTrue.as_view()),
     path("retrieve/<str:pk>", views.RetrieveView.as_view()),
     path("", views.CreateView.as_view()),
     path("<str:pk>", views.UpdateView.as_view()),
     path("<str:pk>", views.DeleteView.as_view()),
]