document.querySelector('.div3').addEventListener('click', function() {
    alert('div3 Clicked');
});

document.querySelector('.div2').addEventListener('click', function() {
    alert('div2 Clicked');
});

document.querySelector('.div1').addEventListener('click', function() {
    alert('div1 Clicked');
});

// მოვლენების ახსნა: 

// Bubbling - როდესაც ვაჭერთ div3-ს, პირველ რიგში გამოვა div3 Clicked, შემდეგ div2 Clicked, და ბოლოს div1 Clicked

// Capturing - როდესაც ვაჭერთ div3-ს, პირველ რიგში გამოვა div1 Clicked, შემდეგ div2 Clicked, და ბოლოს div3 Clicked


