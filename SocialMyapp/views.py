from django.views.generic import TemplateView
from allauth.account.views import SignupView, LoginView, PasswordResetView

class Home(TemplateView):
    template_name = 'home.html'

class MySignupView(SignupView):
    template_name = 'signup.html'

class MyLoginView(LoginView):
    template_name = 'login.html'

class MyPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'



