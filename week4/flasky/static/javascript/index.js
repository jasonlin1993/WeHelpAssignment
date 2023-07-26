function Check(event) {
    let checkForm = document.getElementById("check");
    if (!checkForm.checked) {
        alert("請先點擊同意條款");
        event.preventDefault(); // 阻止表單提交
    }
}

// 2. 最後一題，我們會從前端用 JavaScript 直接把使用者導向到 /square/正整數，不要從後端再轉一次。
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