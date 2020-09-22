//Ex 1

// function myMove() {
// 	console.log("working")
// 	var elem = document.getElementById("animate");
// 	var pos = 0;
// 	var id = setInterval(frame, 5);
// 	function frame(){
// 		if (pos == 350){
// 			clearInterval(id);
// 		}else {
// 			pos++;
// 			elem.style.left = pos + "px";
// 			elem.style.left = pos + "px"; 
// 				}
// 	}
// }



// Ex 2

// const fill = document.querySelector('.fill');
// const empties = document.querySelectorAll('.empty');


// fill.addEventListener('dragstart', dragStart);
// fill.addEventListener('dragend', dragEnd);


// // console.log(empties)
// for (const empty of empties) {
// 	empty.addEventListener('dragover', dragOver);
// 	empty.addEventListener('dragenter', dragEnter);
// 	empty.addEventListener('dragleave', dragLeave);
// 	empty.addEventListener('drop', dragDrop);
// }


// function dragStart() {
// 	this.className += 'hold';
// }

// function dragEnd() {
// 	this.className = 'fill';
// }

// function dragOver(e){
// 	e.preventDefault();
// }

// function dragEnter(e) {
// 	e.preventDefault();
// 	this.className += 'hovered';
// }

// function dragLeave() {
// 	this.className = 'empty';
// }

// function dragDrop() {
// 	this.className = 'empty';
// 	this.append(fill);
// }

        const fill = document.querySelector('.fill');
        const empties = document.querySelectorAll('.empty');

        // Fill listeners
        fill.addEventListener('dragstart', dragStart);
        fill.addEventListener('dragend', dragEnd);

        // Loop through empty boxes and add listeners
        for (const empty of empties) {
            empty.addEventListener('dragover', dragOver);
            empty.addEventListener('dragenter', dragEnter);
            empty.addEventListener('dragleave', dragLeave);
            empty.addEventListener('drop', dragDrop);
        }

        
        // Drag Functions
        function dragStart() {
            this.className += ' hold';
            // setTimeout(() => (this.className = 'invisible'), 0);
        }

        function dragEnd() {
            this.className = 'fill';
        }

        function dragOver(e) {
            e.preventDefault();
        }

        function dragEnter(e) {
            e.preventDefault();
            this.className += ' hovered';
        }

        function dragLeave() {
            this.className = 'empty';
        }

        function dragDrop() {
            this.className = 'empty';
            this.append(fill);
        }