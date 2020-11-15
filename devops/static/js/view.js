const viewGlobal = document.querySelector('.view-global');
const viewUnit = document.querySelector('.view-unit');
const pagination = document.querySelector('.pagination');

viewGlobal.addEventListener('click', ()=>{
    viewGlobal.parentElement.classList.remove('active')
    pagination.classList.remove('exist');
});

viewUnit.addEventListener('click', ()=>{
    viewUnit.parentElement.classList.add('active')
    pagination.classList.add('exist');
});