var farm = document.querySelector("#farm");
var count = 1;
var game;

function spon(event) {
  var chick = document.getElementById("b"+count);
  chick.setAttribute('size', 'c');
  var xPosition = event.clientX - farm.getBoundingClientRect().left - (chick.clientWidth / 2);
  var yPosition = event.clientY - farm.getBoundingClientRect().top - (chick.clientHeight / 2);
  chick.style.left = xPosition + "px";
  chick.style.top = yPosition + "px";
  chick.setAttribute('x', xPosition);
  chick.setAttribute('y', yPosition);
  count++;
  chick.setAttribute('size', 'c');
  chick.setAttribute('grow', 1);
}
function walk(){
  var numC = Math.floor(Math.random()*5+1);
  var chick = document.getElementById("b"+numC);
  num = Math.floor(Math.random()*5);
  var walking = 50*(num == 1 || num == 2) + -50*(num == 3 || num == 4);
  if (chick.getAttribute('grow') == 1){
    numR = Math.floor(Math.random()*3);
    var x = chick.getAttribute('x');
    var y = chick.getAttribute('y');
    x = Number(x);
    y = Number(y);
    x += walking*(numR%2 == 0)*(x+walking > -50 && x+walking < 1200);
    y += walking*(numR%2 == 1)*(y+walking > -50 && y+walking< 500);
    chick.style.left = x + "px";
    chick.style.top = y + "px";
    chick.setAttribute('x', x);
    chick.setAttribute('y', y);
  }
}
game = setInterval(walk, 300);

farm.addEventListener("click", spon);
