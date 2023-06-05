from django.urls import path
from accounts.views import user_login, user_logout

urlpattern = [
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout")
]
