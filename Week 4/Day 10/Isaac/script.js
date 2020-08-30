//FUNCTIONS

//DECLARING
// function myFunction(name, age) {

//     console.log("My name is " + name + " my age is " + age);
// }

// //INVOKING
//myFunction('Isaac', 80);


// myFunction("Sarah", 22);
// myFunction("Ben", 40);



// FUNCTIONS WITHOUT PARAMETERS

// Declare the function
// function greet (){

// 	alert('Hello World');

// }


// // Execute the function
//  greet();




// FUNCTIONS WITH PARAMETERS

// function sum(number1, number2){

//     var resultado = number1 + number2;
    
// 	console.log(resultado);

// }

// sum(21, 4);
// sum(10, 5);
// sum(5, 9);


//UNDEFINES (because dont ask her age)

// function myFunction(name, age) {
//     console.log("My name is " + name + " my age is "  + age) // age undefined 
// }

// myFunction("Sarah")




// FUNCTIONS WITH RETURN

// function sum(number1, number2){

//     var result = number1 + number2;
    
// 	return result;

// }

// console.log(sum(1, 2));



// function myFunction(name, age) {

//     var result = "My name is " + name + " my age is "  + age 

//     return result 
// }

// var girl = myFunction("Sarah", 22)

// console.log(girl) // girl  = result



// function myFunction(name, age) {

//     if (name == "Sarah") {

//         var result = "Hey " + name 

//         return result 

//     } else {

//         return "You are not the right person"
//     }
// }

// var girl = myFunction("Sarah", 22)

// console.log(girl) // girl  = Hey Sarah



//RETURN WILL STOP THE FUNCTION

// Every function in JavaScript returns undefined unless otherwise specified. 
// When a function returns a value, 
// it's returning a result The return value is "returned" back to the "caller" of the function


// function myFunction(name, age) {

//     var result = "My name is " + name + " my age is "  + age 

//     return "hey";
    
//     return result ;
// }


// var girl = myFunction("Sarah", 22);

// console.log(girl) // girl  = "hey";



// function myFunction(name, age) {

//     if (name != "Sarah") {

//         return;

//         return 'oh its that person again';
//     } 

//     alert ("You are not the right person")
// }

// var girl = myFunction("Isaac", 22)

// console.log(girl) // girl  = undefined







//setInterval(function, time in milliseconds);

// var secondHand = 0;


// function count(){

//     ++secondHand;
    
//     console.log(secondHand);
    
// }

// count();



// setInterval(function(){

//     ++secondHand;
    
//     console.log(secondHand);
    
// }, 1000);







//setTimeout(funcion, time in milliseconds);

// var text = 'Hello World';

// setTimeout(greet, 1000);

// function greet(){

// 	console.log(text);
// }






// SCOPE
// Scope refers to the visibility of variables. In other words, 
// which parts of your program can see or use it. Normally, 
// every variable has a global scope. 
// Once defined, every part of your program can access a variable.


//LOCAL VARIABLE


// function myFunction(name, age) {

//     var eye_color = "blue";

//     console.log("My name is " + name + " my age is "  + age + " I have " + eye_color + " eyes");
// }

// myFunction("Sarah", 22)

// console.log(eye_color) // undefined



// Local Variable - Declared inside a function

// function sayGooobye(){

// 	var saygooobye = 'Bye, see you later';

// 	alert(saygooobye);

// }

// //sayGooobye();

// console.log(saygooobye);



//GLOBAL

// Global Variable - Declared outside of a function

// var message = 'Hello, I am a variable';

// function greet (){

// 	alert(message);
// }

//  //greet();

//  console.log(message);



// var eye_color = "blue"

// function myFunction(name, age) {

//     console.log("My name is " + name + " my age is "  + age + " I have " + eye_color + " eyes")
// }

// myFunction("Sarah", 22);

// console.log(eye_color) // blue
