// //Ex 1

// let para= document.getElementsByTagName('p');
// console.log(para);

// for (var i = 0; i < para.length; i++) {
// 	para[i].classList.add('para_article');
// }
// let article = document.querySelector('article');

// let lastPara = article.lastElementChild;
// lastPara.remove();

// let titleH2 = document.querySelector('h2');

// titleH2.addEventListener('click', removeTitle);
// function removeTitle () {
// 	titleH2.remove();
// }

// let bigTitle = document.querySelector('h1');
// let numPx = Math.random()*100;
// bigTitle.style.fontsize = numPx + 'px';

// let firstPara = article.childNodes[5];
// firstPara.addEventListener('click', hidePara);
// function hidePara() {
// 	firstPara.remove();
// }

// let secondPara = article.childNodes[7];
// secondPara.addEventListener('click', delayClick);
// function delayClick() {
// 	setInterval(function (){
// 		if (!secondPara.style.opacity) {
// 			secondPara.style.opacity = 1;
// 		}
// 		if (secondPara.style.opacity > 0) {
// 			secondPara.style.opacity -= 1;
// 		}	else {
// 			clearInterval();
// 		}
// 	}, 2000)
// }

// let newButton = document.createElement('button');
// newButton.innerHTML = 'Submit'
// document.body.appendChild(newButton);



// newButton.addEventListener('click', getInfo);
// function getInfo () {
// let nameInput = document.getElementsByTagName('input')[0].value;
// let opinionInput = document.getElementsByTagName('input')[1].value;
// let table = document.createElement('div');
// document.body.appendChild(table);
// table.innerHTML = "<table border = '1'>" + 
// '<tr>' + '<th>nameInput</th>' + '<th>opinionInput</th>' + '</tr>' +
// '<tr>' + '<td>' + nameInput + '</td>' + '<td>' + opinionInput + '</td>' + '</tr>'



// console.log(nameInput);
// }



// Ex 2

let bolds;

function getBold_items(){
bolds = document.getElementsByTagName('strong')

console.log(bolds)
}

getBold_items()


function highLigth(){
	for(i=0; i<bolds.length; i++){
		bolds[i].style.color = 'blue'
	}
}
highLigth()


function return_normal(){
	for(i=0; i<bolds.length; i++){
		bolds[i].style.color = 'black'
	}
}
return_normal()


function newHighlight(){
let para = document.querySelector('p');
	para.addEventListener('mouseover', highLigth);
	para.addEventListener('mouseout', return_normal);

}
newHighlight()