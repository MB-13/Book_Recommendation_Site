from django.urls import path
from . import views
from Home_Page.views import AddFutureReadView,LogOutView

urlpatterns = [
    path("<str:genre>",views.GenreView.as_view(),name="Genre"),
    path("add-to-frl/",AddFutureReadView.as_view(),name="genre-add-frl"),
    path("logout/",LogOutView.as_view(),name="genre-logout"),
]
