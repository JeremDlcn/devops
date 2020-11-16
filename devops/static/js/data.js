let route = window.location.origin + '/data'
console.log(route);
fetch(route, {
     method: 'GET'
})
.then(r => r.json())
.then(data => {
    console.log(data); //response
   
    
    // update all charts
    updateChart(data)
});

function updateChart(data) {

    //bar values

    // Temperature en cuve
    barValue[0] = data.bar.tempTank
    bar1Chart.data.datasets.forEach((dataset) => {
        dataset.data.push(barValue[0]);
    });
    bar1Chart.update();

    // Température extérieur
    barValue[1] = data.bar.tempExt
    bar2Chart.data.datasets.forEach((dataset) => {
        dataset.data.push(barValue[1]);
    });
    bar2Chart.update();

    // pH de la cuve
    barValue[2] = data.bar.ph
    bar3Chart.data.datasets.forEach((dataset) => {
        dataset.data.push(barValue[2]);
    });
    bar3Chart.update();

    // K+ de la cuve
    barValue[3] = data.bar.k
    bar4Chart.data.datasets.forEach((dataset) => {
        dataset.data.push(barValue[3]);
    });
    bar4Chart.update();


    // lines charts values
    linesValue[0] = data.lines.nacl
    lineChart.data.datasets.forEach((dataset) => {
        linesValue[0].forEach((elt) => {
            dataset.data.push(elt);
        })
    })
    lineChart.update();

    //bacteria values
    linesValue[1] = data.lines.bacteria.salmonelle
    linesValue[2] = data.lines.bacteria.ecoli
    linesValue[3] = data.lines.bacteria.listeria
    // lineChart2.data.datasets.forEach((dataset) => {
    //     linesValue[1].forEach((elt) => {
    //         dataset.data.push(elt);
    //     })
    //     linesValue[2].forEach((elt) => {
    //         dataset.data.push(elt);
    //     })
    //     linesValue[3].forEach((elt) => {
    //         dataset.data.push(elt);
    //     })
    //     console.log(dataset.data);
    // })
    for (let i = 0; i < lineChart2.data.datasets.length; i++){
        idx = i + 1
        linesValue[idx].forEach((elt)=>{
            lineChart2.data.datasets[i].data.push(elt)
        })
    }
    lineChart2.update();


}