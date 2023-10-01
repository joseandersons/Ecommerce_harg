from django.http import JsonResponse

from clientes.models import Cliente
from .models import Pedido, ItemPedido
import json


def adicionar_carrinho(request):
    if request.method == "POST":
        data = json.loads(request.body)
        product_id = data.get("product_id")
        produto_nome = data.get("produto")
        preco = data.get("preco")
        imagem = data.get("imagem")
        quantity = data.get("quantity")

        if isinstance(request.user, Cliente):
            cliente = request.user.cliente
            pedido, created = Pedido.objects.get_or_create(usuario=cliente, status="C", defaults={"total": 0})

            subtotal = preco * quantity
            item_pedido = ItemPedido(
                pedido=pedido,
                produto=produto_nome,
                produto_id=product_id,
                preco=preco,
                quantidade=quantity,
                imagem=imagem,
                subtotal=subtotal
            )
            item_pedido.save()

            pedido.total += subtotal
            pedido.save()
        else:
            # Para visitantes, armazene o carrinho na sessão
            cart = request.session.get('cart', [])
            cart.append({
                'product_id': product_id,
                'produto': produto_nome,
                'preco': preco,
                'imagem': imagem,
                'quantity': quantity
            })
            request.session['cart'] = cart

        return JsonResponse({"success": True})

    return JsonResponse({"success": False, "message": "Método não permitido"}, status=405)
