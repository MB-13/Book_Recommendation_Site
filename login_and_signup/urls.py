from django.urls import path
from . import views

urlpatterns = [
    path("register",views.UserRegisterView.as_view(),name="register"),
    path("",views.UserLoginView.as_view(),name="login"),
    path("reset",views.resetView.as_view(),name="reset"),
    path("password-reset/<email>",views.changePassView.as_view(),name="change")
]
