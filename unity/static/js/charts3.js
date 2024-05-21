// Define los datos del gráfico
const data = {
  labels: [
      'January',
      'February',
      'March',
      'April'
  ],
  datasets: [{
      type: 'bar',
      label: 'Bar Dataset',
      data: [10, 20, 30, 40],
      borderColor: 'rgb(255, 99, 132)',
      backgroundColor: 'rgba(255, 99, 132, 0.2)'
  }, {
      type: 'line',
      label: 'Line Dataset',
      data: [50, 50, 50, 50],
      fill: false,
      borderColor: 'rgb(54, 162, 235)'
  }]
};

// Esperar a que el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', function() {
  // Obtén el contexto del canvas
  const ctx = document.getElementById('myChart3').getContext('2d');

  // Crea el gráfico
  const myChart = new Chart(ctx, {
      type: 'bar',
      data: data,
      options: {}
  });
});
