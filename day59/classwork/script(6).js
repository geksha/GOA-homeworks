const userPasswrd = document.getElementById('password').value;
const message = document.getElementById('message');

while (attemps > 0) {
    if (userPassword === correctPassword) {
        alert('Access granted!');
        message.textContent = '';
        return;
    } else {
        attempts--;
        if (attempts > 0) {
            message.textContent = 'Incorrect password. You have $(attemps) attempts left.';
            return;
        } else {
            message.textContent = 'Access denied. No attempts left.';
            alert('Access denied.');
            return;
        }
    }
}