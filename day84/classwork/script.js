const boxes = document.querySelectorAll('.box'); 
const btn = document.getElementById('btn');
const result = document.getElementById('spec');
let turn = "X";
let board = ["", "", "", "", "", "", "", "", ""]; 
let roundWon = false;

boxes.forEach((element, index) => {
    element.innerHTML = "";
    element.addEventListener('click', function() {
        if (element.innerHTML === "" && !roundWon) {
            const p = document.createElement('p');
            p.textContent = turn; 
            p.classList.add('white-text'); 
            element.appendChild(p); 
            p.style.color = turn === "X" ? '#A737FF' : '#1892EA';

            board[index] = turn;

            if (checkWinner()) {
                result.textContent =` ${turn} WIN!`
                roundWon = true; 
            } else {
                turn = turn === "X" ? "O" : "X"; 
            }
        }
    });
});

const winCases = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  
    [0, 4, 8], [2, 4, 6]             
];

function checkWinner() {
    for (let i = 0; i < winCases.length; i++) {
        const [a, b, c] = winCases[i];
        if (board[a] && board[a] === board[b] && board[a] === board[c]) {
            return true; 
        }
    }
    return false; 
}

btn.addEventListener('click', () => {
    result.textContent = ""
    boxes.forEach(box => {
        box.innerHTML = "";
    });
    board = ["", "", "", "", "", "", "", "", ""]; 
    turn = "X"; 
    roundWon = false;
});