from django.urls import path
from chatapp import views

app_name = 'chatapp'  # Define the app namespace

urlpatterns = [
    path("", views.index, name="chat"),
    path("friend/<int:id>", views.friend, name="friend")
]
