const optionsBarCharts = [
    {
        type: 'bar',
        data: { labels: [["cuve","(°C)"]], datasets: [{ label: ["°C"], backgroundColor: ["#2CE00F"], barThickness: 40, data: '' }]},
        options: { responsive: true, maintainAspectRatio: false, legend: { display: false },
            scales: {
                yAxes: [{ ticks: {fontSize: 10, min: 2, stepSize: 0.1, suggestedMax: 4.5}  }],
                xAxes: [{ ticks: {fontSize: 10, maxRotation: 0}  }]
            }
            }
    },
    {
        type: 'bar',
        data: { labels: [["ext","(°C)"]], datasets: [{ label: ["°C"], backgroundColor: ["#2CE00F"], barThickness: 40, data: '' }]},
        options: { responsive: true, maintainAspectRatio: false, legend: { display: false },
            scales: {
                yAxes: [{ ticks: {fontSize: 10, min: 7.5, stepSize: 0.1, suggestedMax: 14.5}  }],
                xAxes: [{ ticks: {fontSize: 10, maxRotation: 0}  }]
            }
            }
    },
    {
        type: 'bar',
        data: { labels: ["pH"], datasets: [{ label: ["pH"], backgroundColor: ["#2CE00F"], barThickness: 40, data:''}]},
        options: { responsive: true, maintainAspectRatio: false, legend: { display: false },
            scales: {
                yAxes: [{ ticks: {fontSize: 10, min: 6.5, suggestedMax: 7.5, stepSize: 0.1, beginAtZero: true}  }],
                xAxes: [{ ticks: {fontSize: 10, maxRotation: 0}  }]
            }
            }
    },
    {
        type: 'bar',
        data: { labels: [["K+","(mg)"]], datasets: [{ label: ["K+"], backgroundColor: ["#2CE00F"], barThickness: 40, data: '' }]},
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
    bars1.push(new Chart(bar1Charts[i], optionsBarCharts[0]))
    bars2.push(new Chart(bar2Charts[i], optionsBarCharts[1]))
    bars3.push(new Chart(bar3Charts[i], optionsBarCharts[2]))
    bars4.push(new Chart(bar4Charts[i], optionsBarCharts[3]))
}







                    








// Lines charts
// ////////////
const optionsLinesCharts = [
    {
        type: 'line',
        data: {
            labels: ["00", "10", "20", "30"],
            datasets: [{label: 'NaCl', borderColor: "rgba(78, 115, 223, 1)", data:''},]
        }, 
        options: { responsive: true, maintainAspectRatio: false, legend: {labels: {fontSize: 10}},scales: {yAxes: [{ticks: {min: 1,suggestedMax: 2,stepSize: 0.1,}}]} }
    },
    {
        type: 'line',
        data: {
            labels: ["1", "2", "3", "4","5","6","7","8","9"],
            datasets: [
                { label: 'Salmonelle', borderColor: "rgba(78, 115, 223, 1)", data: '' },
                { label: 'E-coli', borderColor: "rgba(255, 75, 103, 1)", data: '' },
                { label: 'Listéria', borderColor: "rgba(73, 224, 15, 1)", data: '' },
            ]
        }, 
        options: { responsive: true, maintainAspectRatio: false, legend: {labels: {fontSize: 10}},scales: {yAxes: [{ticks: {min: 15,suggestedMax: 55,stepSize: 0.1,}}]} }
    }
];


let line1Charts = document.querySelectorAll(`.line1`);
let line2Charts = document.querySelectorAll(`.line2`);


let lines1 = [];
let lines2 = [];

for (let i = 0; i < 5; i++){
    lines1.push(new Chart(line1Charts[i], optionsLinesCharts[0]))
    lines2.push(new Chart(line2Charts[i], optionsLinesCharts[1]))
}








