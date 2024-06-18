from django.urls import path
from .views import IndexView, Redirecionamento
from django.contrib.auth import views as logar

urlpatterns = [
        path("", IndexView.as_view(), name = "index"),
        path("redirecionamento/", Redirecionamento.as_view(), name = "redirecionamento"),
        path("login/", logar.LoginView.as_view(template_name="login.html"), name="login"),
        path("loginconta/", logar.LoginView.as_view(template_name="loginConta.html"), name="loginConta"),
        path("logout/", logar.LogoutView.as_view(), name="logout"),
]