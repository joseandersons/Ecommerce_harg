from decimal import Decimal, InvalidOperation
from django.shortcuts import redirect, render
from .models import Produto, Grupo  # Importe seu modelo aqui

def cadastrar_produto(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        grupo_id = request.POST.get('grupo')
        preco_original = request.POST.get('preco_original')
        preco_promocional = request.POST.get('preco_promocional')
        imagem = request.FILES.get('imagem')  # Se for um campo de arquivo
        pausado = request.POST.get('pausado')
        
        
        try:
            if preco_original:
                preco_original = Decimal(preco_original)
            if preco_promocional:
                preco_promocional = Decimal(preco_promocional)
        except InvalidOperation:
            # Tratar erro aqui
            pass
        
        grupo = None
        if grupo_id:
           grupo = Grupo.objects.get(id_grupo=grupo_id)

        
        produto = Produto(
            nome=nome,
            descricao=descricao,
            grupo=grupo,
            preco_original=preco_original,
            preco_promocional=preco_promocional,
            imagem=imagem,
            pausado=pausado,
        )
        produto.save()
        
        return redirect('consulta_produtos')
    else:
        grupos = Grupo.objects.all()
        context = {'grupos': grupos}
        return render(request, 'cadastro-produto.html', context)
