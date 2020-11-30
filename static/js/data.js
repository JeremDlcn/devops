//  Fichier de récupération des données provenant de l'API
//  

//Mise à jour toutes les minutes
(init())
setInterval(() => {
    init();
    console.log('test');
}, 60000);


//récupération des dernières données de la base
function init() {
    fetch(window.location.origin + '/data', {
         method: 'GET'
    })
    .then(r => r.json())
    .then(data => {
        // mise a jour de tout les graphiques
        for (let i = 0; i < data.length; i++){
            updateChart(data[i])
        }
    });
}

// Liste de tout les selecteurs d'automates
let robot = document.querySelectorAll('.robot');

// Detection de la sélection d'un automate par l'utilisateur
for (let i = 0; i < robot.length; i++){
    robot[i].addEventListener('change',()=>{
        getData(i + 1,robot[i].value)
    });
}

// récupération des données selon l'unité et l'automate
// Parameters: 
//   unit(number): numéro de l'unité
//   robot(number): numéro de l'automate
function getData(unit, robot) {
    let route = window.location.origin + `/robot?unit=${unit}&robot=${robot}`
    fetch(route, {
        method: 'GET'
    })
    .then(r => r.json())
    .then(data => {
        //mise a jour des graphiques
        updateChart(data)
    });
}


// Fonction de mise à jour des graphiques
// Parameters:
//    data: données contenant les informations provenant de la bdd
function updateChart(data) {
    //transformation et insertion du timestamp en data lisible
    let datt = new Date(data.info.timestamp * 1000).toLocaleString('fr-FR');
    document.querySelector(`.unit[data-unit="${data.info.unit}"] .datetime`).innerText = datt;

    //Valeurs concernant le poids
    document.querySelector(`.unit[data-unit="${data.info.unit}"] .weight-tank`).innerText = data.weight.tank;
    document.querySelector(`.unit[data-unit="${data.info.unit}"] .weight-prod`).innerText = data.weight.product;

    //Valeurs pour les graphiques en Bar
    let bars1Unit = bars1[data.info.unit - 1];
    let bars2Unit = bars2[data.info.unit - 1];
    let bars3Unit = bars3[data.info.unit - 1];
    let bars4Unit = bars4[data.info.unit - 1];

    //remise à zéro des valeurs
    bars1Unit.data.datasets[0].data = [];
    bars2Unit.data.datasets[0].data = [];
    bars3Unit.data.datasets[0].data = [];
    bars4Unit.data.datasets[0].data = [];

    //Température de la cuve
    bars1Unit.data.datasets.forEach((dataset) => {
        dataset.data.push(data.bar.tempTank);
    })
    bars1Unit.update();//mise à jour du graphique


    // Température extérieur
    bars2Unit.data.datasets.forEach((dataset) => {
        dataset.data.push(data.bar.tempExt);
    })
    bars2Unit.update();//mise à jour du graphique


    // pH de la cuve
    bars3Unit.data.datasets.forEach((dataset) => {
        dataset.data.push(data.bar.ph);
    })
    bars3Unit.update();//mise à jour du graphique


    // K+ de la cuve
    bars4Unit.data.datasets.forEach((dataset) => {
        dataset.data.push(data.bar.k);
    })
    bars4Unit.update();//mise à jour du graphique



    //Graphiques avec lignes
    let linesValue = [];
    
    let lines1Unit = lines1[data.info.unit - 1];
    let lines2Unit = lines2[data.info.unit - 1];

    //remise à zéro des graphiques en lignes
    lines1Unit.data.datasets[0].data = []
    lines2Unit.data.datasets[0].data = []
    lines2Unit.data.datasets[1].data = []
    lines2Unit.data.datasets[2].data = []

    // Insertion de la concentration de NaCl
    linesValue[0] = data.lines.nacl
    lines1Unit.data.datasets.forEach((dataset) => {
        linesValue[0].forEach((elt) => {
            dataset.data.push(elt);
        })
    })
    lines1Unit.update(); //mise à jour du graphique

    //Insertion des niveaux de bactéries
    linesValue[1] = data.lines.bacteria.salmonelle
    linesValue[2] = data.lines.bacteria.ecoli
    linesValue[3] = data.lines.bacteria.listeria
    for (let i = 0; i < lines2Unit.data.datasets.length; i++){
        idx = i + 1
        linesValue[idx].forEach((elt)=>{
            lines2Unit.data.datasets[i].data.push(elt)
        })
    }
    lines2Unit.update(); //mise à jour du graphique
}