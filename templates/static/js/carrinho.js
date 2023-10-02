window.addEventListener("DOMContentLoaded", () => {
    let cartItems = JSON.parse(localStorage.getItem('carrinho')) || [];
    let cartDisplayArea = document.getElementById('cartDisplayArea');

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

    let totalDisplay = document.createElement('p');
    totalDisplay.innerText = `Total: R$${subtotal.toFixed(2)}`;
    cartDisplayArea.appendChild(totalDisplay);

    let finalizeDiv = document.createElement('div');
    finalizeDiv.className = 'finalize-control'

    let finalizeButton = document.createElement('button');
    finalizeButton.innerText = 'Finalizar Pedido';
    finalizeButton.className = 'finalize-button'
    finalizeButton.addEventListener('click', () => {
        window.location.href = '/finalizar-pedido/'; 
    });
    finalizeDiv.appendChild(finalizeButton)
    cartDisplayArea.appendChild(finalizeButton);

});

function updateLocalStorage(cartItems) {
    localStorage.setItem('carrinho', JSON.stringify(cartItems));
}
