const child = document.querySelector('.child');
const parent = document.querySelector('.parent');
const containerWidth = document.querySelector('.container').offsetWidth;

let position = 0;
let movingRight = true;

setInterval(() => {
    if (movingRight) {
        position += 1;
        if (position >= containerWidth - 50) {
            movingRight = false;
        }
    } else {
        position -= 1;
        if (position <= 0) {
            movingRight = true;
        }
    }
    child.style.left = position + 'px';
}, 30);

