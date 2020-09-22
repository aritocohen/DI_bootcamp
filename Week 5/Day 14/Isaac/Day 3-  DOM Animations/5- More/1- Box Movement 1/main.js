// window.onload = () => {
//   startSetTimeoutAnimation();
//   startAnimFrameAnimation();
// };

function startSetTimeoutAnimation() {
  const refreshRate = 1000 / 60;
  const maxXPosition = 400;
  let rect = document.getElementById('box-1');
  let speedX = 1;
  let positionX = 0;

  window.setInterval(() => {
    positionX = positionX + speedX;  //move transition
    if (positionX > maxXPosition || positionX < 0) {
      speedX = speedX * (-1);
    }
    rect.style.left = positionX + 'px';
  }, refreshRate);
}








// function startAnimFrameAnimation() {
//   const refreshRate = 1000 / 60;
//   const maxXPosition = 400;
//   let rect = document.getElementById('box-1');
//   let speedX = 1;
//   let positionX = 0;
//
//   function step() {
//     positionX = positionX + speedX;
//     if (positionX > maxXPosition || positionX < 0) {
//       speedX = speedX * (-1);
//     }
//     rect.style.left = positionX + 'px';
//     window.requestAnimationFrame(step);
//   }
//
//   window.requestAnimationFrame(step);
// }
