let courseID = 1234;

const data = {
  datasets: [{
    data: [4.5, 0.5],
    backgroundColor: [
      'rgb(39, 93, 56)',
      'rgba(255, 255, 255, 0)'
    ],
    hoverOffset: 4
  }]
};

const config = {
  type: 'doughnut',
  data: data,
  options: {
    plugins: {
      tooltip: {
        enabled: false
      }
    },
    events: [],
    cutout: "70%"
  }
};

const myChart = new Chart(
  document.getElementById('doughnutChart'),
  config
);
