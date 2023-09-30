

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
    var produtos = document.querySelectorAll('.card');
    var quantidadeDisplay = document.getElementById('quantidadeDisplay');
    var adicionarBtn = document.getElementById('adicionarQuantidade');

    adicionarBtn.addEventListener('click', function() {
        var currentQuantity = parseInt(quantidadeDisplay.innerText, 10);
        quantidadeDisplay.innerText = currentQuantity + 1;
    });

    produtos.forEach(function(produto) {
        produto.addEventListener('click', function() {
            var nome = this.querySelector('.card-title').innerText;
            var descricao = this.querySelector('.card-text').innerText;
            var imagemSrc = this.querySelector('.card-img-top').src;

            // Reset the quantity display to 1
            quantidadeDisplay.innerText = '1';

            document.getElementById('produtoNome').innerText = nome;
            document.getElementById('produtoDescricao').innerText = descricao;
            document.getElementById('produtoImagem').src = imagemSrc;

            var modal = new bootstrap.Modal(document.getElementById('produtoModal'));
            modal.show();
        });
    });
});
