let preveiwContainer = document.querySelector('.product-preview');
let previewBox = preveiwContainer.querySelectorAll('.preview');

document.querySelectorAll('.products-container .product').forEach(product => {
    product.onclick = () => {
        preveiwContainer.style.display = 'flex';
        let name = product.getAttribute('data-name');
        previewBox.forEach(preview => {
            let target = preview.getAttribute('data-target')
            if (name == target) {
                preview.classList.add('active');
            }
        });
    };
});


// var popViews = document.querySelectorAll('.product-preview');
// var popupBtns = document.querySelectorAll('.dry-dtn');
// var closeBtns = document.querySelectorAll('.close-btn');

// // JS for View Button
// var popup = function(popupClick) {
//     popViews[popupClick].classList.add('active');
// }

// popupBtns.forEach((popupBtn, i) => {
//     popupBtn.addEventListener("click", () => {
//         popup(i);
//     });
// });