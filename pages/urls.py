from django.urls import include, path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/consulta-grupo/', views.consulta_grupo, name='consulta_grupos'),
    path('dashboard/consulta-produtos/', views.consulta_produtos, name='consulta_produtos'),
    
    path('dashboard/cadastrar-produto/', include('produto.urls')),
    

] 