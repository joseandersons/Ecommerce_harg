from decimal import Decimal, InvalidOperation
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import Produto, Grupo 


def consulta_produtos(request):
    produtos = Produto.objects.filter(user=request.user)
    return render(request, 'consulta-produtos.html', {'produtos': produtos})

def consulta_grupos(request):
    grupos = Grupo.objects.filter(user=request.user)
    return render(request, 'consulta-grupos.html', {'grupos': grupos})


def cadastrar_produto(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        grupo_id = request.POST.get('grupo')
        preco_original = request.POST.get('preco_original')
        preco_promocional = request.POST.get('preco_promocional')
        imagem = request.FILES.get('imagem') 
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

        loja = request.user.loja
    
        produto = Produto(
            nome=nome,
            descricao=descricao,
            grupo=grupo,
            preco_original=preco_original,
            preco_promocional=preco_promocional,
            imagem=imagem,
            pausado=pausado,
            user=loja
        )
        produto.save()
        
        return redirect('lojas:cadastros:consulta_produtos')
    else:
        grupos = Grupo.objects.filter(user=request.user)
        context = {'grupos': grupos}
        return render(request, 'cadastro-produto.html', context)


def atualizar_status_produto(request, produto_id):
    produto = get_object_or_404(Produto, id_produto=produto_id)
    
    if request.method == "GET":
        novo_status = 'S' if produto.pausado == 'N' else 'N'
        produto.pausado = novo_status
        produto.save()
        return redirect('lojas:cadastros:consulta_produtos')
    else:
        return redirect('lojas:cadastros:consulta_produtos')
    


def alterar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id_produto=produto_id)

    if request.method == "POST":
        produto.nome = request.POST.get('nome', produto.nome)
        produto.descricao = request.POST.get('descricao', produto.descricao)
        grupo_id = request.POST.get('grupo')
        
        if grupo_id:
            produto.grupo = Grupo.objects.get(id_grupo=grupo_id)
        try:
            produto.preco_original = Decimal(request.POST.get('preco_original', produto.preco_original))
            produto.preco_promocional = Decimal(request.POST.get('preco_promocional', produto.preco_promocional))
        except InvalidOperation:
            # Tratar erro aqui
            pass

        nova_imagem = request.FILES.get('imagem')
        if nova_imagem:
            produto.imagem = nova_imagem
        
        produto.pausado = request.POST.get('pausado', produto.pausado)

        produto.save()
        
        return redirect('lojas:cadastros:consulta_produtos')

    else:
        grupos = Grupo.objects.filter(user=request.user)
        context = {'grupos': grupos, 'produto': produto}
        return render(request, 'alterar-produto.html', context)



def deletar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id_produto=produto_id)
    produto.delete()
    messages.success(request, 'Produto deletado com sucesso.')
    return redirect('lojas:cadastros:consulta_produtos')



    
    
def cadastrar_grupo(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        pausado = request.POST.get('pausado')
        
        loja = request.user.loja
        grupo = Grupo(
            nome=nome,
            pausado=pausado,
            user=loja
        )
        grupo.save()
        
        return redirect('lojas:cadastros:consulta_grupos')
    else:
        return render(request, 'cadastro-grupo.html')
    
def deletar_grupo(request, id_grupo):
    grupo = get_object_or_404(Grupo, id_grupo=id_grupo)

    Produto.objects.filter(grupo_id=id_grupo).delete()
    
    grupo.delete()
    messages.success(request, 'Grupo deletado com sucesso.')
    return redirect('lojas:cadastros:consulta_grupos')


def atualizar_status_grupo(request, id_grupo):
    grupo = get_object_or_404(Grupo, id_grupo=id_grupo)
    
    if request.method == "GET":
        novo_status = 'S' if grupo.pausado == 'N' else 'N'
        grupo.pausado = novo_status
        grupo.save()
        return redirect('lojas:cadastros:consulta_grupos')
    else:
        return redirect('lojas:cadastros:consulta_grupos')


def alterar_grupo(request, id_grupo):
    grupo = get_object_or_404(Grupo, id_grupo=id_grupo)

    if request.method == "POST":
        grupo.nome = request.POST.get('nome', grupo.nome)        
        grupo.pausado = request.POST.get('pausado', grupo.pausado)
        grupo.save()
        
        return redirect('lojas:cadastros:consulta_grupos')

    else:
        context = {'grupo': grupo}
        return render(request, 'alterar-grupo.html', context)
