
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
