// Ex 1

let navBar = document.querySelector('#navBar');
navBar.setAttribute('id', 'socialNetworkNavigation');

// console.log(navBar);

let ul = document.querySelector('ul');
let newLi = document.createElement('li');
let newA = document.createElement('a');
newA.innerHTML = 'Logout';
newA.href = '#';
newLi.appendChild(newA);

// console.log(newLi)

ul.appendChild(newLi);

