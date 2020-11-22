let barValue = []
const optionsCharts = [
    {
        type: 'bar',
        data: { labels: [["cuve","(°C)"]], datasets: [{ label: ["°C"], backgroundColor: ["#2CE00F"], barThickness: 40, data: barValue[0] }]},
        options: { responsive: true, maintainAspectRatio: false, legend: { display: false },
            scales: {
                yAxes: [{ ticks: {fontSize: 10, min: 2, stepSize: 0.1, suggestedMax: 4.5}  }],
                xAxes: [{ ticks: {fontSize: 10, maxRotation: 0}  }]
            }
            }
    },
    {
        type: 'bar',
        data: { labels: [["ext","(°C)"]], datasets: [{ label: ["°C"], backgroundColor: ["#2CE00F"], barThickness: 40, data: barValue[1] }]},
        options: { responsive: true, maintainAspectRatio: false, legend: { display: false },
            scales: {
                yAxes: [{ ticks: {fontSize: 10, min: 7.5, stepSize: 0.1, suggestedMax: 14.5}  }],
                xAxes: [{ ticks: {fontSize: 10, maxRotation: 0}  }]
            }
            }
    },
    {
        type: 'bar',
        data: { labels: ["pH"], datasets: [{ label: ["pH"], backgroundColor: ["#2CE00F"], barThickness: 40, data: barValue[2] }]},
        options: { responsive: true, maintainAspectRatio: false, legend: { display: false },
            scales: {
                yAxes: [{ ticks: {fontSize: 10, min: 6.5, suggestedMax: 7.5, stepSize: 0.1, beginAtZero: true}  }],
                xAxes: [{ ticks: {fontSize: 10, maxRotation: 0}  }]
            }
            }
    },
    {
        type: 'bar',
        data: { labels: [["K+","(mg)"]], datasets: [{ label: ["K+"], backgroundColor: ["#2CE00F"], barThickness: 40, data: barValue[3] }]},
        options: { responsive: true, maintainAspectRatio: false, legend: { display: false },
            scales: {
                yAxes: [{ ticks: {fontSize: 10,  min: 30, suggestedMax: 50,  setSize: 1, beginAtZero: true}  }],
                xAxes: [{ ticks: {fontSize: 10, maxRotation: 0}  }]
            }
            }
    }
];

let bar1Charts = document.querySelectorAll(`.bar1`);
let bar2Charts = document.querySelectorAll(`.bar2`);
let bar3Charts = document.querySelectorAll(`.bar3`);
let bar4Charts = document.querySelectorAll(`.bar4`);

let bars1 = [];
let bars2 = [];
let bars3 = [];
let bars4 = [];

for (let i = 0; i < 5; i++){
    bars1.push(new Chart(bar1Charts[i], optionsCharts[0]))
    bars2.push(new Chart(bar2Charts[i], optionsCharts[1]))
    bars3.push(new Chart(bar3Charts[i], optionsCharts[2]))
    bars4.push(new Chart(bar4Charts[i], optionsCharts[3]))
}







                    








// Lines charts
// ////////////
let linesValue = [];

let chart1 = document.getElementById('chart1').getContext('2d');
let chart2 = document.getElementById('chart2').getContext('2d');



let lineChart = new Chart(chart1, {
    type: 'line',
    data: {
        labels: ["00", "10", "20", "30"],
        datasets: [
            {
                label: 'NaCl',
                borderColor: "rgba(78, 115, 223, 1)",
                data: linesValue[0],
            },
        ]
    }, 
    options: {
        responsive: true,
        maintainAspectRatio: false,
        legend: {
            labels: {
                fontSize: 10
            }
        },
        scales: {
            yAxes: [{
                ticks: {
                    min: 1,
                    suggestedMax: 2,
                    stepSize: 0.1,
                }
            }],
        }
    }
});


let lineChart2 = new Chart(chart2, {
    type: 'line',
    data: {
        labels: ["00", "10", "20", "30", "40", "50", "60"],
        datasets: [
            {
                label: 'Salmonelle',
                borderColor: "rgba(78, 115, 223, 1)",
                data: linesValue[1],
            },
            {
                label: 'E-coli',
                borderColor: "rgba(255, 75, 103, 1)",
                data: linesValue[2],
            },
            {
                label: 'Listéria',
                borderColor: "rgba(73, 224, 15, 1)",
                data: linesValue[3],
            },
        ]
    }, 
    options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            yAxes: [{
                ticks: {
                    min: 15,
                    suggestedMax: 55,
                }
            }],
        }
    }
});