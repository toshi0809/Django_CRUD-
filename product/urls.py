from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="root"),
    path("create", views.create, name="create"),
    path("add", views.add, name="add"),
    path("<int:id>", views.edit, name="edit"),
    path("<int:id>/update", views.edit, name="update"),
    path("<int:id>/delete", views.delete, name="delete"),
]
