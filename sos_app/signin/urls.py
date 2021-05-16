from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views as core_views

urlpatterns = [
    url(r"^$", core_views.home, name="home"),
    url(
        r"^login/$",
        auth_views.LoginView.as_view(template_name="login.html"),
        name="login",
    ),
    url(
        r"^logout/$",
        auth_views.LogoutView.as_view(template_name="home.html"),
        name="logout",
    ),
    url(r"^signup/$", core_views.signup, name="signup"),
]
