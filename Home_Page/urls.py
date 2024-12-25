from django.urls import path
from . import views

urlpatterns = [
    path("",views.HomeView.as_view(),name="home"),
    path("add_to_frl/",views.AddFutureReadView.as_view(),name="add_to_frl"),
    path("remove_from_frl/",views.RemoveFutureReadView.as_view(),name="remove_from_frl"),
    path("logout/",views.LogOutView.as_view(),name="logout"),
]
