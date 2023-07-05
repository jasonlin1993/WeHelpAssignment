document.addEventListener('DOMContentLoaded', function() {
    // 獲取元素
    let menuCheckbox = document.querySelector('.menu__checkbox');
    let headerItemMobile = document.querySelector('.header__item--mobile');

    // 當 .menu__checkbox 被點擊時，阻止事件的傳播
    menuCheckbox.addEventListener('click', function(event) {
    event.stopImmediatePropagation();
    });

    // 當點擊的元素不是 .header__item--mobile 或其子元素時，隱藏 .header__item--mobile
    document.addEventListener('click', function(event) {
    let isClickInside = headerItemMobile.contains(event.target);
    if (!isClickInside) {
        // 要在隱藏 .header__item--mobile 時取消選中 .menu__checkbox
        menuCheckbox.checked = false;
    }
    });
  });