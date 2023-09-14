from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/cadastros/', include('produto.urls')),
    
    path('login/', include('perfil.urls')),
    
] 