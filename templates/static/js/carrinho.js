window.addEventListener("DOMContentLoaded", () => {
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }

    let cartItems = JSON.parse(localStorage.getItem('carrinho')) || [];
    let cartDisplayArea = document.getElementById('cartDisplayArea');

    var cart_quantity = cartItems.reduce(function (acumulador, item) {
        return acumulador + item.quantity;
    }, 0)

    document.getElementById('cart-quantity').innerText = cart_quantity + "x";

    let subtotal = 0;
    cartItems.forEach((item, index) => {
        let cartItemDiv = document.createElement('div');
        cartItemDiv.className = 'cart-item';

        // Add item image
        let itemImage = document.createElement('img');
        itemImage.src = item.imagem_url;
        itemImage.alt = item.produto;
        itemImage.className = 'cart-item-image';
        cartItemDiv.appendChild(itemImage);

        // Add item name
        let itemName = document.createElement('p');
        itemName.innerText = item.produto;
        itemName.className = 'cart-item-name';
        cartItemDiv.appendChild(itemName);

        // Add item price
        let itemPrice = document.createElement('p');
        itemPrice.innerText = `R$${item.preco}`;
        itemPrice.className = 'cart-item-price';
        cartItemDiv.appendChild(itemPrice);

        // Quantity control
        let quantityDiv = document.createElement('div');
        quantityDiv.className = 'quantity-control';

        let decreaseButton = document.createElement('button');
        decreaseButton.innerText = '-';
        decreaseButton.className = 'quantity-button';
        decreaseButton.addEventListener('click', () => {
            if (item.quantity > 1) {
                item.quantity--;
                updateLocalStorage(cartItems);
                itemQuantity.innerText = item.quantity;
            }
        
        });
        quantityDiv.appendChild(decreaseButton);

        let itemQuantity = document.createElement('p');
        itemQuantity.innerText = item.quantity;
        itemQuantity.className = 'item-quantity';
        quantityDiv.appendChild(itemQuantity);

        let increaseButton = document.createElement('button');
        increaseButton.innerText = '+';
        increaseButton.className = 'quantity-button';
        increaseButton.addEventListener('click', () => {
            item.quantity++;
            updateLocalStorage(cartItems);
            itemQuantity.innerText = item.quantity;
        });
        quantityDiv.appendChild(increaseButton);

        cartItemDiv.appendChild(quantityDiv);

        // Delete button
        let deleteButton = document.createElement('button');
        deleteButton.innerText = 'X';
        deleteButton.className = 'delete-button';
        deleteButton.addEventListener('click', () => {
            cartItems.splice(index, 1);
            updateLocalStorage(cartItems);
            cartItemDiv.remove();
        });
        cartItemDiv.appendChild(deleteButton);

        // Append the cart item div to the cartDisplayArea
        cartDisplayArea.appendChild(cartItemDiv);

        subtotal += item.preco * item.quantity;
    });

    let totalDiv = document.createElement('div')
    totalDiv.className = 'total-control'

    let totalDisplay = document.createElement('p');
    totalDisplay.innerText = `Total: R$${subtotal.toFixed(2)}`;

    totalDiv.appendChild(totalDisplay)
    cartDisplayArea.appendChild(totalDiv);

    


    let paymentDiv = document.createElement('div');
    paymentDiv.className = 'payment-control';

    // Criando e estilizando o título "Forma de Pagamento"
    let paymentTitle = document.createElement('p');
    paymentTitle.innerText = 'Forma de Pagamento';
    paymentTitle.style.textAlign = 'center';  // Centralizar o texto
    paymentDiv.appendChild(paymentTitle);

    // Função de criação para opções de pagamento (Dinheiro e Cartão)
    function createPaymentOption(name, value) {
        let optionDiv = document.createElement('div');
        optionDiv.className = 'payment-option';
        optionDiv.style.display = 'flex';
        optionDiv.style.justifyContent = 'center';  // Centraliza horizontalmente os elementos no container
        optionDiv.style.marginBottom = "10px";  // Espaçamento na parte inferior

        let radio = document.createElement('input');
        radio.type = 'radio';
        radio.name = 'paymentMethod';
        radio.value = value;
        radio.id = value;
        optionDiv.appendChild(radio);

        let label = document.createElement('label');
        label.innerText = ' ' + name;  // Espaço antes para não ficar grudado no input
        label.htmlFor = value;
        label.style.marginLeft = "5px";  // Pequeno espaçamento à esquerda
        optionDiv.appendChild(label);

        paymentDiv.appendChild(optionDiv);
    }

    // Cria opções de pagamento
    createPaymentOption('Dinheiro', 'dinheiro');
    createPaymentOption('Cartão', 'cartao');

    // Adiciona o div principal de pagamento ao cartDisplayArea
    cartDisplayArea.appendChild(paymentDiv);




    let finalizeDiv = document.createElement('div');
    finalizeDiv.className = 'finalize-control'
    finalizeDiv.id = 'finalize-button'

    let finalizeButton = document.createElement('button');
    finalizeButton.innerText = 'Finalizar Pedido';
    finalizeButton.className = 'finalize-button'

    finalizeDiv.appendChild(finalizeButton);
    cartDisplayArea.appendChild(finalizeDiv);



    document.getElementById('finalize-button').addEventListener('click', function() {
        let cartItems = JSON.parse(localStorage.getItem('carrinho')) || [];
        
        let selectedPaymentOption = document.querySelector('input[name="paymentMethod"]:checked');
    
        if (!selectedPaymentOption) {
            alert('Por favor, selecione uma forma de pagamento.');
            return;
        }
    
        let selectedPaymentMethod = selectedPaymentOption.value;
    

        $.ajax({
            url: '/adicionar-item-carrinho/finalizar-pedido/',
            method: 'POST',
            data: JSON.stringify({
                list_items:cartItems,
                paymentMethod: selectedPaymentMethod 
            }),
            contentType: 'application/json; charset=utf-8',
            dataType: 'json',
            success: function(response) {
                if(response.success) {
                    alert('Produto(s) comprado(s) com sucesso!');

                    cartItems = [];
                    updateLocalStorage(cartItems);
                    while (cartDisplayArea.firstChild) {
                        cartDisplayArea.removeChild(cartDisplayArea.firstChild);
                    }

                    if (response.redirect_url) {
                        window.location.href = response.redirect_url;
                    }



                } else {
                    alert('Erro na compra!');
                }
            },
            error: function() {
                alert('Erro ao comunicar com o servidor. Tente novamente.');
            }
        })
    });

});

function updateLocalStorage(cartItems) {
    localStorage.setItem('carrinho', JSON.stringify(cartItems));
}

