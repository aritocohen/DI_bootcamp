var newParagraph = document.createElement('p');

var newText = document.createTextNode('Hello, I am a new text');

newParagraph.appendChild(newText);

newParagraph.setAttribute('class', 'text');

// var container = document.getElementsByClassName('container')[0];




// Select the parent element of an element

var firstParagraph = document.getElementsByClassName('text')[0];

var parentParagraphs = firstParagraph.parentNode;

//console.log(parentParagraphs);



parentParagraphs.className = 'container';


// Place the item before the selected one

var paragraphs = document.getElementsByClassName('text');

parentParagraphs.insertBefore(newParagraph, paragraphs[2]);
