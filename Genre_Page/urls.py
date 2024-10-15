from django.urls import path
from . import views

urlpatterns = [
    path("<str:genre>",views.GenreView.as_view(),name="Genre"),
]
