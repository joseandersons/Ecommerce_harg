from django.urls import include, path
from . import views

urlpatterns = [
    path('login-cliente', views.login_cliente, name='login_cliente'),
    
] 