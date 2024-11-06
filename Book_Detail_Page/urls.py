from django.urls import path
from . import views

urlpatterns = [
    path("<int:Id>",views.DetailView.as_view(),name="book"),
]