// 1. 定義 API URL
let url = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json';
let loadedElements = 3;
let results = [];

fetch(url)
    .then(response => response.json()) 
    .then(data => {
        results = data.result.results;
        
        for(let i=0; i<3; i++){
            let newDiv = document.createElement("div");
            newDiv.className = "container__section__Promotion";
            let fileString = results[i].file;
            let firstUrl = fileString.split('https')[1];
            firstUrl = 'https' + firstUrl;
            let titleName = document.createElement("p");
            let img = document.createElement('img');
            img.src = firstUrl;
            img.className = "container__section__Promotion__picture" ;
            titleName.className = "container__section__Promotion__text";
            titleName.innerText = results[i].stitle; 
            newDiv.appendChild(img);
            newDiv.appendChild(titleName);
            document.querySelector('.container__section').appendChild(newDiv);
        }

        loadElements();
    });

function loadElements() {
    for(let i = loadedElements; i < Math.min(loadedElements + 12, results.length); i++){
        let newDiv = document.createElement("div");
        newDiv.className = "container__section__title";
        let fileString = results[i].file;
        let firstUrl = fileString.split('https')[1];
        firstUrl = 'https' + firstUrl;

        let titleName = document.createElement("p");
        let img = document.createElement('img');
        img.src = firstUrl;
        img.className = "container__section__title__image" ;
        titleName.className = "container__section__title__text";

        titleName.innerText = results[i].stitle; 

        newDiv.appendChild(img);
        newDiv.appendChild(titleName);

        document.querySelector('.container__section').appendChild(newDiv);
    }

    loadedElements += 12;

    if (loadedElements >= results.length) {
        document.querySelector('.container__button--load').style.display = 'none';
    }
}

document.querySelector('.container__button--load').addEventListener('click', loadElements);