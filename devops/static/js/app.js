let chart1 = document.getElementById('chart1').getContext('2d');
let chart2 = document.getElementById('chart2').getContext('2d');
let chart3 = document.getElementById('chart3').getContext('2d');
let chart4 = document.getElementById('chart4').getContext('2d');


new Chart(document.getElementById("bar1"), {
    type: 'bar',
    data: {
        labels: [
            ["Température","Cuve (°C)"],
            ["Température","extérieur (°C)"],
            "NaCl",
            "K+"
        ],
        datasets: [{
            label: ["°C","ext°C","NaCl","K+"],
            backgroundColor: ["#c45850","#c45850","#c45850","#c45850"],
            barThickness: 40,
            data: [40, 20, 30, 40]
        }]
    },
    options: {
        legend: {
          display: false // hides the legend
        },
        scales: {
            yAxes: [{
                ticks: {
                    min: 0,
                    beginAtZero: true
                }
            }],
        }
      }
});





// Lines charts

let lineChart = new Chart(chart1, {
    type: 'line',
    data: {
        labels: ["00", "10", "20", "30", "40", "50", "60"],
        datasets: [
            {
                label: 'Montagne russe',
                borderColor: "rgba(78, 115, 223, 1)",
                data: [2.5, 2.5, 2.8, 2.0, 3.0, 2.8, 4.0],
            },
            {
                label: 'Montagne Française',
                borderColor: "rgba(255, 75, 103, 1)",
                data: [2.2, 2.0, 1.8, 2.8, 3.9, 1.0, 2.0],
            },
        ]
    }, 
    options: {
        scales: {
            xAxes: [
                {
                    position: "botom",
                    scaleLabel: {
                        display: true,
                        labelString: "Frequency (Hz)"
                    }
                }
            ],
            yAxes: [
                {
                    position: "top",
                    scaleLabel: {
                        display: true,
                        labelString: "Frequency (Hz)",
                    }
                }
            ],
        }
    }
});

let lineChart2 = new Chart(chart2, {
    type: 'line',
    data: {
        labels: ["00", "10", "20", "30", "40", "50", "60"],
        datasets: [
            {
                label: 'Montagne russe',
                borderColor: "rgba(78, 115, 223, 1)",
                data: [2.5, 2.5, 2.8, 2.0, 3.0, 2.8, 4.0],
            },
            {
                label: 'Montagne Française',
                borderColor: "rgba(255, 75, 103, 1)",
                data: [2.2, 2.0, 1.8, 2.8, 3.9, 1.0, 2.0],
            },
        ]
    }, 
    options: {
        scales: {
            xAxes: [
                {
                    position: "botom",
                    scaleLabel: {
                        display: true,
                        labelString: "Frequency (Hz)"
                    }
                }
            ],
            yAxes: [
                {
                    position: "top",
                    scaleLabel: {
                        display: true,
                        labelString: "Frequency (Hz)",
                    }
                }
            ],
        }
    }
});

let lineChart3 = new Chart(chart3, {
    type: 'line',
    data: {
        labels: ["00", "10", "20", "30", "40", "50", "60"],
        datasets: [
            {
                label: 'Montagne russe',
                borderColor: "rgba(78, 115, 223, 1)",
                data: [2.5, 2.5, 2.8, 2.0, 3.0, 2.8, 4.0],
            },
            {
                label: 'Montagne Française',
                borderColor: "rgba(255, 75, 103, 1)",
                data: [2.2, 2.0, 1.8, 2.8, 3.9, 1.0, 2.0],
            },
        ]
    }, 
    options: {
        scales: {
            xAxes: [
                {
                    position: "botom",
                    scaleLabel: {
                        display: true,
                        labelString: "Frequency (Hz)"
                    }
                }
            ],
            yAxes: [
                {
                    position: "top",
                    scaleLabel: {
                        display: true,
                        labelString: "Frequency (Hz)",
                    }
                }
            ],
        }
    }
});

let lineChart4 = new Chart(chart4, {
    type: 'line',
    data: {
        labels: ["00", "10", "20", "30", "40", "50", "60"],
        datasets: [
            {
                label: 'Montagne russe',
                borderColor: "rgba(78, 115, 223, 1)",
                data: [2.5, 2.5, 2.8, 2.0, 3.0, 2.8, 4.0],
            },
            {
                label: 'Montagne Française',
                borderColor: "rgba(255, 75, 103, 1)",
                data: [2.2, 2.0, 1.8, 2.8, 3.9, 1.0, 2.0],
            },
        ]
    }, 
    options: {
        scales: {
            xAxes: [
                {
                    position: "botom",
                    scaleLabel: {
                        display: true,
                        labelString: "Frequency (Hz)"
                    }
                }
            ],
            yAxes: [
                {
                    position: "top",
                    scaleLabel: {
                        display: true,
                        labelString: "Frequency (Hz)",
                    }
                }
            ],
        }
    }
});