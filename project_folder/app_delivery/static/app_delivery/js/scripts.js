// Aguarda o carregamento do DOM
document.addEventListener('DOMContentLoaded', () => {
    
    // Função para simular adição ao carrinho
    const botoesAdicionar = document.querySelectorAll('.btn-outline-danger');

    botoesAdicionar.forEach(botao => {
        botao.addEventListener('click', (event) => {
            event.preventDefault();
            const nomePizza = event.target.closest('.card-body').querySelector('.card-title').innerText;
            alert(`${nomePizza} foi adicionada ao seu carrinho! 🍕`);
        });
    });

    console.log("Interface da Pizzaria carregada com sucesso!");
});