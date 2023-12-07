from datetime import datetime

from django.views.generic import TemplateView

from django.views.generic.edit import CreateView

from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import logout

from django.shortcuts import redirect, render

# Create your views here.


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = "home/register.html"
    success_url = "/login"

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("cart.list")
        return super().get(request, *args, **kwargs)


class LogoutInterfaceView(LogoutView):
    success_url = "/login"
    template_name = "home/logout.html"


def logout_view(request):
    if request.method == "POST":
        logout(request)
    return render(request, "home/logout.html")


class LoginInterfaceView(LoginView):
    template_name = "home/login.html"

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("cart.list")
        return super().get(request, *args, **kwargs)


class HomeView(TemplateView):
    template_name = "home/welcome.html"
    extra_context = {"today": datetime.today()}
