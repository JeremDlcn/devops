let route = window.location.origin + '/data'
console.log(route);
fetch(route, {
     method: 'GET'
})
.then(r => r.json())
.then(data => {
    console.log(data); //response
    barValue[0] = data.name

});

function updateChart() {
    bar1Chart.data.datasets.forEach((dataset) => {
        dataset.data.push(barValue[0]);
    });
    bar1Chart.update();
}