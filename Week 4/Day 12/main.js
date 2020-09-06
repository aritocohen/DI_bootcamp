// var btns = document.querySelectorAll("button");
// var result = document.getElementById("result");

//     for (var thisBtn of btns) {
//         thisBtn.addEventListener('click', function() {
//         if (this.innerHTML == "=")
//             result.value = eval(result.value);
//         else if (this.innerHTML == "clear")
//             result.value = "";
//         else
//             result.value += this.innerHTML;
//                 })
//             }

let calcstrg = "";
let display = document.getElementById('display');
	console.log(display);

function my_f (btn){
	calcstrg = calcstrg + btn;
	display.innerHTML = calcstrg;
	console.log(calcstrg)
}

function result(){
	let calcresult = eval(calcstrg);
	display.innerHTML = calcresult;
	console.log(calcstrg + "+" + calcresult);
	calcstrg = calcresult;
}

function calcclear(){
	calcstrg = '';
	display.innerHTML = 0;
}