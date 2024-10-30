from django.urls import path
from . import views

urlpatterns = [
    path("",views.DetailView.as_view(),name="book"),
]