// Fichier de gestion des commandes
//  Changement de vue et pagination
// 
const viewGlobal = document.querySelector('.view-global');
const viewUnit = document.querySelector('.view-unit');
const pagination = document.querySelector('.pagination');

// Changement de vue
viewGlobal.addEventListener('click', ()=>{
    viewGlobal.parentElement.classList.remove('active')
    pagination.classList.remove('exist');
    removeClass();
});

viewUnit.addEventListener('click', ()=>{
    viewUnit.parentElement.classList.add('active')
    pagination.classList.add('exist');
    sortUnit();
    hideUnit(1);
});


// Mise en place de la pagination
const units = document.querySelectorAll('.unit');

function sortUnit() {
    const pages = document.querySelectorAll('.pagination li');
    pages.forEach(element => {
        element.addEventListener('click', ()=>{            
            let nbPage = element.getAttribute("data-page");
            hideUnit(nbPage);
        });
    });
}

function hideUnit(num) {
    for (let i = 0; i < units.length; i++) {
        units[i].style.display = "none"
        if (units[i].getAttribute("data-unit") == num) {
            units[i].style.display = "flex";
            document.querySelector('main').classList.add('only');
        }
    }
}


function removeClass() {
    for (let i = 0; i < units.length; i++) {
        units[i].style.display = "flex"
        document.querySelector('main').classList.remove('only');
    }
}