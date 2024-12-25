from django.urls import path
from . import views
from Home_Page.views import AddFutureReadView,LogOutView

urlpatterns = [
    path("<int:Id>",views.DetailView.as_view(),name="book"),
    path("bestseller/<int:Id>",views.BestSelDetailView.as_view(),name="bestseller"),
    path("add_to_frl/",AddFutureReadView.as_view(),name="bd/add_to_frl"),
    path("logout/",LogOutView.as_view(),name="bd-logout"),
]