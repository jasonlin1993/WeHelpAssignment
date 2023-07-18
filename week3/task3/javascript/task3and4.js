// 1. 定義 API URL
let url = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json';

let loadedElements = 3; // 已經載入的元素數量
let results = []; // 儲存從 API 取得的資料

// 2. 使用 fetch 函數取得 api 資料
fetch(url)
    .then(response => response.json())
    .then(data => {
        results = data.result.results;
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
