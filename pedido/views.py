from urllib import request
from django.http import JsonResponse
from django.shortcuts import render
from clientes.models import Cliente
from produto.models import Produto
from .models import Pedido, ItemPedido
import json
from django.core import serializers


def adicionar_carrinho(request):
    if request.method == "POST":
        data = json.loads(request.body)
        product_id = data.get("product_id")
        quantity = data.get("quantity")
        produto = Produto.objects.get(id_produto=product_id)
        preco = produto.preco_promocional if produto.preco_promocional > "0" else produto.preco_original
        preco = float(preco.replace(',', '.'))
        
        try:
            produto = Produto.objects.get(id_produto=product_id)
        except Produto.DoesNotExist:
            return JsonResponse({'error': 'Produto não encontrado'}, status=404)
    
        # if request.user.is_authenticated:
        #     cliente_name = request.user.username
        #     cliente = Cliente.objects.get(username=cliente_name)
        #     pedido, status = Pedido.objects.get_or_create(usuario=cliente, status="C", loja=produto.user)
        #     print(f'preço {preco} quant {quantity}')
        #     subtotal = preco * quantity
        #     print(f'sub {subtotal}')
        #     item_pedido = ItemPedido(
        #         pedido=pedido,
        #         produto=produto.nome,
        #         produto_id=product_id,
        #         preco=preco,
        #         quantidade=quantity,
        #         imagem=produto.imagem,
        #         subtotal=subtotal
        #     )
        #     item_pedido.save()
        #     pedido.total += subtotal
        #     pedido.save()

        data = {
            'product_id': product_id,
            'produto': produto.nome,
            'preco': preco,
            'imagem_url': produto.imagem.url if produto.imagem else None,
            'quantity': quantity,
            "loja": produto.user.username,
        }

        return JsonResponse({"success": True, 'data': data})

    return JsonResponse({"success": False, "message": "Método não permitido"}, status=405)




def consultar_carrinho(request):
    
    return render(request, 'consultar-carrinho.html')


