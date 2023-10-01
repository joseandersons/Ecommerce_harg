

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


$(document).ready(function() {
    $('#carouselExampleIndicators').carousel({
        interval: 4000 // Define o intervalo entre os slides em milissegundos
    });
});


function scrollLeft() {
    let container = document.getElementById('scrollableArea');
    container.scrollLeft -= 200; // ajuste este valor conforme necessário
}

function scrollRight() {
    let container = document.getElementById('scrollableArea');
    container.scrollLeft += 200; // ajuste este valor conforme necessário
}



document.addEventListener("DOMContentLoaded", function() {
    var produtos = document.querySelectorAll('.card.clickable');
    var modalElement = document.getElementById('produtoModal');
    var adicionarAoCarrinhoBtn = document.getElementById('btnAdicionarAoCarrinho');
    var quantidadeDisplay = document.getElementById('quantidadeDisplay');
    var adicionarBtn = document.getElementById('adicionarQuantidade');

    adicionarBtn.addEventListener('click', function() {
        var currentQuantity = parseInt(quantidadeDisplay.innerText, 10);
        quantidadeDisplay.innerText = currentQuantity + 1;
    });

    produtos.forEach(function(produto) {
        produto.addEventListener('click', function() {
            var nome = produto.querySelector('.card-title').innerText;
            var descricao = produto.querySelector('.card-text').innerText;
            var imagemSrc = produto.querySelector('.card-img-top').src;
            var produtoId = produto.getAttribute('data-produto-id');

            // Reset the quantity display to 1
            quantidadeDisplay.innerText = '1';

            document.getElementById('produtoNome').innerText = nome;
            document.getElementById('produtoDescricao').innerText = descricao;
            document.getElementById('produtoImagem').src = imagemSrc;

            // Associate product ID with the button
            adicionarAoCarrinhoBtn.setAttribute('data-produto-id', produtoId);

            var modal = new bootstrap.Modal(modalElement);
            modal.show();
        });
    });
});

document.getElementById('btnAdicionarAoCarrinho').addEventListener('click', function() {
    var produtoId = this.getAttribute('data-produto-id');
    var quantity = parseInt(document.getElementById('quantidadeDisplay').innerText, 10);

    $.ajax({
        url: '/adicionar-item-carrinho/',  // URL do seu endpoint
        method: 'POST',
        data: JSON.stringify({
            product_id: produtoId,
            quantity: quantity
        }),
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: function(response) {
            if(response.success) {
                alert('Produto adicionado ao carrinho com sucesso!');
                
                // Update cart quantity display
                document.getElementById('cart-quantity').innerText = response.cart_quantity + "x";
            } else {
                alert('Houve um erro ao adicionar o produto ao carrinho: ' + response.message);
            }
        },
        
        
        
        error: function() {
            alert('Erro ao comunicar com o servidor. Tente novamente.');
        }
    });
});


$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
        }
    }
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}