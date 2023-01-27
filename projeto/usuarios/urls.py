from django.contrib.auth import views as auth_views
from django.urls import path

from .views import UsuarioCreate

urlpatterns = [
    #path('endereco/', MinhaView.as_view(), name='nome-da-url'),
    path('login/', auth_views.LoginView.as_view(template_name = 'usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registrar/', UsuarioCreate.as_view(), name='registrar'),
]