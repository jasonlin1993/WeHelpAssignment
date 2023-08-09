function checkForm(event, formId) {
    let form = document.forms[formId];
    for (let i = 0; i < form.elements.length; i++) {
        let element = form.elements[i];
        if (element.type === "text" || element.type === "password") {
            if (element.value.trim() === "") {
                alert("輸入值不可為空白");
                event.preventDefault(); // 阻止表單提交
                return; // 終止函數
            }
        }
    }
}
