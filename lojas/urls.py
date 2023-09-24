from django.urls import include, path
from . import views


app_name = 'lojas'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('cadastros/', include('produto.urls', namespace='cadastros')),
    path('cadastro-loja/', views.criar_conta_loja, name='criar_conta_loja'),
    path('login-loja/', views.login_loja, name='login_loja'),
    path('logout-loja', views.logout_loja, name='logout_loja'),
    
] 