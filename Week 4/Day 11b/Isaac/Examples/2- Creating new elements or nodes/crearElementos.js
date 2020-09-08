// Create new element or node

// <p class="text">'Hello, I am a new text'</p>
// 

// We create a new paragraph
var newParagraph = document.createElement('p');

// We create a new text for the paragraph
var newText = document.createTextNode('Hello, I am a new text');

// Add the new text in the paragraph
newParagraph.appendChild(newText);

// Add a new class attribute
newParagraph.setAttribute('class', 'text');

// Select container
var container = document.getElementsByClassName('container')[0];

// Add the new paragraph inside the container

container.appendChild(newParagraph);






