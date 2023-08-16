function checkForm(event, formId) {
    let form = document.forms[formId];
    for (let i = 0; i < form.elements.length; i++) {
        let element = form.elements[i];
        if (element.type === "text" || element.type === "password") {
            if (element.value.trim() === "") {
                alert("輸入值不可為空白");
                event.preventDefault(); 
                return; 
            }
        }
    }
}

async function fetchMemberData() {
    const username = document.getElementById('usernameInput').value;

    try {
        const response = await fetch(`http://127.0.0.1:3000/api/member?username=${username}`);
        const data = await response.json();
        
        if (data.data) {
            document.querySelector('.container__text__member').textContent = `${data.data.name} (${data.data.username})`;
        } else {
            document.querySelector('.container__text__member').textContent = '查詢不到此會員資訊';
        }

    } catch (e) {
        console.log(e);
    }
}
async function updateName() {
    try {
        const newNameInput = document.querySelector('input[name="newName"]');
        const newUsername = newNameInput.value.trim(); 
        const resultText = document.querySelector(".container__text__member--patch"); 

        if (!newUsername) {
            resultText.textContent = "更新失败";
            return;
        }

        const response = await fetch("http://127.0.0.1:3000/api/member", {
            method: "PATCH",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                name: newUsername
            })
        });

        const data = await response.json();

        if (data.ok) {
            document.getElementById("usernameDisplay").innerText = newUsername;
            resultText.textContent = "成功更新!";
        } else {
            resultText.textContent = "更新錯誤";
        }
    } catch (e) {
        console.log(e);
    }
}
