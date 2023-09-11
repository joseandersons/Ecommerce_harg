
from django.urls import include, path
from . import views

urlpatterns = [

    path('consulta-produtos/', views.consulta_produtos, name='consulta_produtos'),
    path('consulta-grupos', views.consulta_grupos, name='consulta_grupos'),
    path('cadastrar-produto/', views.cadastrar_produto, name='cadastrar_produto'),
    path('cadastrar-grupo/', views.cadastrar_grupo, name='cadastrar_grupo'),
    path('atualizar-status-produto/<int:produto_id>/', views.atualizar_status_produto, name='atualizar_status_produto'),
    path('alterar-produto/<int:produto_id>/', views.alterar_produto, name='alterar_produto'),
    path('deletar-produto/<int:produto_id>/', views.deletar_produto, name='deletar_produto'),

    path('deletar-grupo/<int:id_grupo>/', views.deletar_grupo, name='deletar_grupo'),
    path('atualizar-status-grupo/<int:id_grupo>/', views.atualizar_status_grupo, name='atualizar_status_grupo'),
    path('alterar-grupo/<int:id_grupo>/', views.alterar_grupo, name='alterar_grupo'),
    

] 

