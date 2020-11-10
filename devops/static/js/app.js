let ctx = document.getElementById('chart').getContext('2d');

let lineChart = new Chart(ctx, {
    type: 'line',
    data: [{
        x: 10,
        y: 20
    }, {
        x: 15,
        y: 10
    }],
    // options: options
});