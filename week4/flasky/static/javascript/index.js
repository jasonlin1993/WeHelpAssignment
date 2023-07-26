function Check(event) {
    let checkForm = document.getElementById("check");
    if (!checkForm.checked) {
        alert("請先點擊同意條款");
        event.preventDefault(); // 阻止表單提交
    }
}

function checkNumber(event) {
    event.preventDefault();
    let countValue = document.getElementById("count").value;
    let regex = /^[1-9]\d*$/;
    if (!regex.test(countValue)) {
        alert("請輸入正整數");
    } else {
        location.href = '/square/' + countValue;
    }
}