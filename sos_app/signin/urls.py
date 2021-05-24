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
    url(r"^add/card$", core_views.add_card, name="add_card"),
    url(r"^add/image$", core_views.add_image, name="add_image"),
    url(r"^list/$", core_views.card, name="list"),
    url(r"^list/view/(?P<relation>\d+)$", core_views.card_view, name="card_view"),
    url(r"^list/view/send/service$", core_views.send_services, name="send_card")
]
