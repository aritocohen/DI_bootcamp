// Day 10 Excersie 1

// function checkDriverAge(){
// 	let age = prompt("What is your age?");

// if (Number(age) < 18) {
//     alert("Sorry, you are too young to drive this car. Powering off");
// } else if (Number(age) > 18) {
//     alert("Powering On. Enjoy the ride!");
// } else if (Number(age) === 18) {
//     alert("Congratulations on your first year of driving. Enjoy the ride!");
// }
// }

// checkDriverAge()



// function checkDriverAge(age){
	
// if (Number(age) < 18) {
//     alert("Sorry, you are too young to drive this car. Powering off");
// } else if (Number(age) > 18) {
//     alert("Powering On. Enjoy the ride!");
// } else if (Number(age) === 18) {
//     alert("Congratulations on your first year of driving. Enjoy the ride!");
// }
// }

// checkDriverAge(92)


// Ex 2

// amazonBasket = {
//     glasses: 1,
//     books: 2,
//     floss: 100
// }

// function checkBasket(){
// 	var item = prompt('What item are you looking for?')

// 	if (item in amazonBasket) {
// 		alert('your item is in the basket')
// 	}
// 	else {
// 	alert('your item is not in the basket')
// 	}
// }
// checkBasket()


// Ex 3

// function changeEnough(pocketChange,price){
// 	var sum = 0
// 	sum = sum + pocketChange[0]*0.25
// 	sum = sum + pocketChange[1]*0.10
// 	sum = sum + pocketChange[2]*0.5
// 	sum = sum + pocketChange[3]*0.1

// 	if(sum>=price){
// 		console.log('you have enough money')
// 	}
// 	else{
// 		console.log('you dont have enough money')
// 	}
// }

// // changeEnough([2, 100, 0, 0], 14.11)

// changeEnough([0, 0, 20, 5], 0.75)



// Ex 4

// var shoppingList = ['banana', 'orange', 'apple'];

// let stock = { 
//     "banana": 6, 
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry":1
// }  

// let prices = {    
//     "banana": 4, 
//     "apple": 2, 
//     "pear": 1,
//     "orange": 1.5,
//     "blueberry":10
// } 

// function myBill = (){
// 	for(item of shoppingList){
// 		if (stock[item] > 0) {
// 			sumOfPrices = sumOfPrices + prices[item]
// 		}
// 		sumOfPrices += prices[i];
// 	}
// 	return sumOfPrices:
// }
// console.log(myBill());


// Ex 5

// function random(begin, end){
// 	if (begin%2 === 1){
// 		begin++
// 	}for(i = begin; i <= end; i+=2){
// 	console.log(i)
// 	}
// }

// random(0, 100)



//Ex 6

// var sum= 0;
// function multiplesOf23(number){
// 	for(var i = 1; i< number; i++){
// 		if ((i % 23 == 0)){
// 			sum=sum+i
// 		}
// 	}
// 	return sum;
// }
// console.log(multiplesOf23(500))



// Ex 7

function hotelCost(){
	var night= prompt ('How many nights would you like to stay in the Hotel?');
	var cost= Number(night)*140
	return cost;
}