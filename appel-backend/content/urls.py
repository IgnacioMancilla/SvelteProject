from django.urls import path
from .views import login_view, me_view, logout_view

urlpatterns = [
    path("auth/login/",  login_view,  name="login"),
    path("auth/me/",     me_view,     name="me"),
    path("auth/logout/", logout_view, name="logout"),
]

