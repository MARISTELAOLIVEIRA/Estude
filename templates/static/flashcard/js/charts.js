const ctx = document.getElementById('grafico1');
const dadosData = JSON.parse(document.getElementById('dados-data').textContent);
const categoriasData = JSON.parse(document.getElementById('categorias-data').textContent);
const acertosCatData = JSON.parse(document.getElementById('acertos-cat-data').textContent);
      
new Chart(ctx, {
    type: 'pie',
    data: {
        labels: ['Acertos', 'Erros'],
        datasets: [{
            label: 'Qtd',
            data: dadosData,
            borderWidth: 1
        }]
    },
    
});

const ctx2 = document.getElementById('grafico2');
      
new Chart(ctx2, {
    type: 'radar',
    data: {
        labels: categoriasData,
        datasets: [{
            label: 'Quantidade',
            data: acertosCatData,
            borderWidth: 1,
            fill: true,
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgb(255, 99, 132)',
            pointBackgroundColor: 'rgb(255, 99, 132)',
            pointBorderColor: '#fff',
            pointHoverBackgroundColor: '#fff',
            pointHoverBorderColor: 'rgb(255, 99, 132)'
        }]
    },
          
});