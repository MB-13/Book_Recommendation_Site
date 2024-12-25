from django.urls import path
from . import views
from Home_Page.views import AddFutureReadView,LogOutView

urlpatterns = [
    path("",views.SearchView.as_view(),name="search"),
    path("search-suggestions/",views.SearchSuggestionsView.as_view(),name='search_suggestions'),
    path("search-result/",views.SearchResultView.as_view(),name="search_result"),
    path("add_to_frl/",AddFutureReadView.as_view(),name="search-add-frl"),
    path("logout/",LogOutView.as_view(),name="search-logout"),
]