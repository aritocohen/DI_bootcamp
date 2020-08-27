
//FOR LOOPS

//Syntax

/* for(variable start; length or condition; increment){

	Code we want to repeat

 }
 */    


// for (isaac = 0; isaac < 5; isaac++) {

//       console.log("The number is " + isaac);
//   }


// for(var i = 1; i <= 101; i++){

//  	console.log(i);

//  }


// var week = ['Sunday','Monday','Tuesday','Wednesday','Thursday', 'Friday', 'Saturday']

//  for(var i = 0; i < week.length; i++){

//  	console.log(week[i]);

//  }





//FOR IN

//(its more for objects)

// var person = {
//                fname: "John", 
//                lname: "Doe", 
//                age: 25
//              };

// for (x in person) {

//   console.log(person[x]) // John Doe 25

// }


// var week = ['Sunday','Monday','Tuesday','Wednesday','Thursday', 'Friday', 'Saturday'];

//  for(yitzjak in week){

//  	console.log(week[yitzjak]);
//  }



//FOR OF 

//(its more for arrays than objects)

var colors = ["blue", "yellow", "red"];

// for ( i in colors) {
//    console.log(i); // logs "0", "1", "2",
// }


// for (i of colors) {

//    console.log(i); // logs blue, yellow, red
// }




//WHILE LOOPS


// SINTAX

// while(condition){
//
// }

// var n = 0;

// while (n < 3) {

//  console.log(n)

//   n++;

  
// }



// var i = 1;

// while(i < 11){

//   document.write(i + '<br>');
  
// 	i++;

// }



//DO WHILE

// i = 1;

// do {
//   console.log(i);

//   i++;
// }

// while (i <= 10);



//Do while loop - Run the code at least 1 time

// var i = 12;

// do{

//   document.write(i + '<br>');
  
//   i++;
  
// }while(i < 11);




//Break Statement


// for (i = 0; i < 10; i++) {

//   if (i === 3) { 

//       break;

//     }

//   console.log(i); // 0 1 2
// }


// BREAK - Allows you to stop the cycle

// var week = ['Sunday','Monday','Tuesday','Wednesday','Thursday', 'Friday', 'Saturday'];


// for(var i = 0; i < week.length; i++){


//   //console.log(i);

// 	console.log(week[i]);

// 	if (week[i] == 'Wednesday') {
    
// 		break;
// 	}

// }




//OTHER WAY OF EXECUTION

// var week = ['Sunday','Monday','Tuesday','Wednesday','Thursday', 'Friday', 'Saturday'];


// for(var i = 0; i < week.length; i++){
	

// 	if (week[i] == 'Wednesday') {
    
// 		break;
//   }
  

//   console.log(week[i]);


// }





//CONTINUE

// for (i = 0; i < 10; i++) {

//   if (i === 3) { 

//     continue;   //skip it , we aer skipping number 3

//   }

//   console.log(i); // 0 1 2 4 5 6 7 8 9 
// }



// CONTINUE - Lets you jump to the next execution of the cycle

// var week = ['Sunday','Monday','Tuesday','Wednesday','Thursday', 'Friday', 'Saturday'];

// for(var i = 0; i < week.length; i++){

// 	if (week[i] == 'Thursday') {

// 		continue;
// 	}

// 	console.log(week[i]);

// }



//INFINTE LOOP (DANGER)


// for (var i = 0; i < Infinity; i++) {

//     //console.log(i);
// }



// while(true){

//   console.log('VIRUS');

// }




