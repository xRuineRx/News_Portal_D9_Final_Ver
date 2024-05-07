from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, TemplateView
from .views import BaseRegisterView
from .views import upgrade_me

urlpatterns = [
    path('login/',
         LoginView.as_view(template_name = 'flatpages/sign/login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name = 'flatpages/sign/logout.html'),
         name='logout'),
    path('logout/confirm/',
         TemplateView.as_view(template_name = 'flatpages/sign/logout_confirm.html'),
         name='logout_confirm'),
    path('signup/',
         BaseRegisterView.as_view(template_name='flatpages/sign/signup.html'),
         name='signup'),
    path('be_author/', upgrade_me, name='be_author'),
]