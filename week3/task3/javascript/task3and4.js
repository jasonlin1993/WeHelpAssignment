// 1. 定義 API URL
let url = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json';
let loadedElements = 3;
let results = [];

function createElement(result, divClass, imgClass, textClass) {
    let newDiv = document.createElement("div");
    newDiv.className = divClass;
    let fileString = result.file;
    let firstUrl = fileString.split('https')[1];
    firstUrl = 'https' + firstUrl;
    let titleName = document.createElement("p");
    let img = document.createElement('img');
    img.src = firstUrl;
    img.className = imgClass;
    titleName.className = textClass;
    titleName.innerText = result.stitle;
    newDiv.appendChild(img);
    newDiv.appendChild(titleName);
    document.querySelector('.container__section').appendChild(newDiv);
}

fetch(url)
    .then(response => response.json()) 
    .then(data => {
        results = data.result.results;
        
        for(let i=0; i<3; i++){
            createElement(
                results[i],
                'container__section__Promotion',
                "container__section__Promotion__picture",
                "container__section__Promotion__text"
            )
        }

        loadElements();
    });

function loadElements() {
    for(let i = loadedElements; i < Math.min(loadedElements + 12, results.length); i++){
        createElement(
            results[i],
            "container__section__title",
            "container__section__title__image",
            "container__section__title__text"
        );
    }

    loadedElements += 12;

    if (loadedElements >= results.length) {
        document.querySelector('.container__button--load').style.display = 'none';
    }
}

document.querySelector('.container__button--load').addEventListener('click', loadElements);