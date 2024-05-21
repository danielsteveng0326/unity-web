// charts.js

function inicializarGrafico() {
    // Datos para el gráfico
    const labels = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio'];
    const data = {
        labels: labels,
        datasets: [{
            label: 'Contratación',
            data: [65, 59, 80, 81, 56, 55, 40],
            backgroundColor: [
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)'
            ],
            borderColor: [
                'rgb(54, 162, 235)',
                'rgb(54, 162, 235)',
                'rgb(54, 162, 235)',
                'rgb(54, 162, 235)',
                'rgb(54, 162, 235)',
                'rgb(54, 162, 235)',
                'rgb(54, 162, 235)'
            ],
            borderWidth: 1
        }]
    };

    // Configuración del gráfico
    const config = {
        type: 'bar',
        data: data,
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    grid: {
                        display: false, // Oculta las líneas de la cuadrícula
                    },
                    ticks: {
                        display: false, // Oculta las etiquetas de la escala
                    }
                }
            }
        }
    };
    

    // Obtener el contexto del canvas y dibujar el gráfico
    const ctx = document.getElementById('myChart').getContext('2d');
    new Chart(ctx, config);
}

// Llamar a la función cuando la página esté completamente cargada
document.addEventListener("DOMContentLoaded", function() {
    inicializarGrafico();
});
