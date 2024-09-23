const div = document.querySelector('#parent')

console.dir(div);

div.removeChild(div.children[1])

div.firstElementChild.remove()