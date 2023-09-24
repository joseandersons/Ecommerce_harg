
from django.urls import include, path
from . import views

app_name = 'cadastros'

urlpatterns = [
    
    path('produtos/', views.consulta_produtos, name='consulta_produtos'),
    path('grupos/', views.consulta_grupos, name='consulta_grupos'),
    path('produto/adicionar/', views.cadastrar_produto, name='cadastrar_produto'),
    path('grupo/adicionar/', views.cadastrar_grupo, name='cadastrar_grupo'),
    path('produto/<int:produto_id>/status/', views.atualizar_status_produto, name='atualizar_status_produto'),
    path('produto/<int:produto_id>/editar/', views.alterar_produto, name='alterar_produto'),
    path('produto/<int:produto_id>/remover/', views.deletar_produto, name='deletar_produto'),
    path('grupo/<int:id_grupo>/remover/', views.deletar_grupo, name='deletar_grupo'),
    path('grupo/<int:id_grupo>/status/', views.atualizar_status_grupo, name='atualizar_status_grupo'),
    path('grupo/<int:id_grupo>/editar/', views.alterar_grupo, name='alterar_grupo'),
]


