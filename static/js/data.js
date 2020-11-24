let route = window.location.origin + '/data'
fetch(route, {
     method: 'GET'
})
.then(r => r.json())
.then(data => {
    // update all charts
    for (let i = 0; i < data.length; i++){
        updateChart(data[i])
    }
});

function updateChart(data) {

    //info value
    document.querySelector(`.unit[data-unit="${data.info.unit}"] .datetime`).innerText = data.info.timestamp;

    //weight values
    document.querySelector(`.unit[data-unit="${data.info.unit}"] .weight-tank`).innerText = data.weight.tank;
    document.querySelector(`.unit[data-unit="${data.info.unit}"] .weight-prod`).innerText = data.weight.product;

    //Bar values
    let bars1Unit = bars1[data.info.unit - 1];
    let bars2Unit = bars2[data.info.unit - 1];
    let bars3Unit = bars3[data.info.unit - 1];
    let bars4Unit = bars4[data.info.unit - 1];

    bars1Unit.data.datasets[0].data = [];
    bars2Unit.data.datasets[0].data = [];
    bars3Unit.data.datasets[0].data = [];
    bars4Unit.data.datasets[0].data = [];

    //Température de la cuve
    bars1Unit.data.datasets.forEach((dataset) => {
        dataset.data.push(data.bar.tempTank);
    })
    bars1Unit.update();


    // Température extérieur
    bars2Unit.data.datasets.forEach((dataset) => {
        dataset.data.push(data.bar.tempExt);
    })
    bars2Unit.update();


    // pH de la cuve
    bars3Unit.data.datasets.forEach((dataset) => {
        dataset.data.push(data.bar.ph);
    })
    bars3Unit.update();


    // K+ de la cuve
    bars4Unit.data.datasets.forEach((dataset) => {
        dataset.data.push(data.bar.k);
    })
    bars4Unit.update();




    let linesValue = [];
    
    // lines charts values
    // concentration de Nacl
    let lines1Unit = lines1[data.info.unit - 1];
    let lines2Unit = lines2[data.info.unit - 1];

    //reset before adding a number
    lines1Unit.data.datasets[0].data = []
    lines2Unit.data.datasets[0].data = []
    lines2Unit.data.datasets[1].data = []
    lines2Unit.data.datasets[2].data = []

    linesValue[0] = data.lines.nacl
    lines1Unit.data.datasets.forEach((dataset) => {
        linesValue[0].forEach((elt) => {
            dataset.data.push(elt);
        })
    })
    lines1Unit.update();

    //bacteria values
    linesValue[1] = data.lines.bacteria.salmonelle
    linesValue[2] = data.lines.bacteria.ecoli
    linesValue[3] = data.lines.bacteria.listeria
    for (let i = 0; i < lines2Unit.data.datasets.length; i++){
        idx = i + 1
        linesValue[idx].forEach((elt)=>{
            lines2Unit.data.datasets[i].data.push(elt)
        })
    }
    lines2Unit.update();
}