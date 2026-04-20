from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import EmailAuthenticationForm

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='usuarios/login.html',
        authentication_form=EmailAuthenticationForm
    ), name='login'),
    # LogoutView by default handles GET locally if we format carefully, but Django 5+ requires POST for logout by default. 
    # For now we'll map it normally.
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
]
