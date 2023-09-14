
window.addEventListener('DOMContentLoaded', event => {

    // Toggle the side navigation
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

});

let cartItems = 0;  // Este valor seria dinamicamente atualizado com base nos itens do carrinho

// Função para adicionar um item ao carrinho
function addItemToCart() {
    cartItems++;
    document.getElementById("cart-count").textContent = cartItems + "x";
}

// Função para remover um item do carrinho
function removeItemFromCart() {
    if (cartItems > 0) {
        cartItems--;
        document.getElementById("cart-count").textContent = cartItems + "x";
    }
}
