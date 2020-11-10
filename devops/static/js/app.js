let ctx = document.getElementById('chart').getContext('2d');

let lineChart = new Chart(ctx, {
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