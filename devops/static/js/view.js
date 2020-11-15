const viewGlobal = document.querySelector('.view-global');
const viewUnit = document.querySelector('.view-unit');

viewGlobal.addEventListener('click', ()=>{
    viewGlobal.parentElement.classList.remove('active')
});

viewUnit.addEventListener('click', ()=>{
    viewUnit.parentElement.classList.add('active')
});