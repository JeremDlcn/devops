let robot = document.querySelectorAll('.robot');

for (let i = 0; i < robot.length; i++){
    robot[i].addEventListener('change',()=>{
        getData(i + 1,robot[i].value)
    });
}

function getData(unit, robot) {
    let route = window.location.origin + `/robot?unit=${unit}&robot=${robot}`
    fetch(route, {
        method: 'GET'
    })
    .then(r => r.json())
    .then(data => {
        updateChart(data)
    });
}