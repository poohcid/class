var farm = document.querySelector("#farm");
var count = 1;
var game;
var chicken = [0, 0, 0, 0, 0, 0, 0, 0];
var CheckFood=0;
var CountFood=[0, 0, 0, 0, 0, 0, 0, 0];
var egg = [0, 0, 0, 0, 0, 0, 0, 0];
var Enemy = [0, 0, 100, 50];
var EnemyR;
var money = 500;
var gun=1;
var start1 = 1;
var enemyCount = 1;
var shop=0;

function gameplay(){
  document.getElementById("money").innerHTML = "Money : "+money;
  Enemy[1]++;
  if (start1 == 1){
    start1 = 0;
    start();
  }
  walk();
  grow();
  if (Enemy[0] < Enemy[1]){
    document.getElementById("enemy").setAttribute('size','c');
  }
  if (document.getElementById("enemy").getAttribute('size') == 'c'){
    enemyTime();
  }
}

function spon(event) {
  if (shop == 1){
      shop = 0;
  for (var i=0; i < 8; i++){
    if (chicken[i] == 0){
      count = i+1;
      chicken[i] = 1;
      break;
    }
  }
  var chick = document.getElementById("b"+count);
  chick.setAttribute('size', 'c');
  var xPosition = event.clientX - farm.getBoundingClientRect().left - (chick.clientWidth / 2);
  var yPosition = event.clientY - farm.getBoundingClientRect().top - (chick.clientHeight / 2);
  chick.setAttribute('grow', 1);
  chick.style.left = xPosition + "px";
  chick.style.top = yPosition + "px";
  chick.setAttribute('x', xPosition);
  chick.setAttribute('y', yPosition);
  chick.setAttribute('size', 'c');
  chick.setAttribute('grow', 1);
}
}

function grow(){
    var x = 0;
    var add=1;
    var typeBox = Math.floor(Math.random()*9);
    x = document.getElementById("b"+typeBox).getAttribute('grow');
    x = Number(x);
    var In = Number(typeBox-1);
    if (CountFood[In] > 0){
      add += 3;
      CountFood[In]--;
    }
    if (x != 0 && x < 100){
        x += add;
        document.getElementById("b"+typeBox).setAttribute('grow', x);
    }
    if (x >= 5 && (Math.floor(Math.random() * 6) == 5) && egg[In] == 0){
      egg[In] = 1;
      document.getElementById("e"+typeBox).setAttribute('size', 'e');
      document.getElementById("e"+typeBox).style.left = Number(document.getElementById("b"+typeBox).getAttribute('x'))+"px";
      document.getElementById("e"+typeBox).style.top = Number(document.getElementById("b"+typeBox).getAttribute('y'))+"px";
    }
    if (x >= 5){
      document.getElementById("b"+typeBox).setAttribute('src', 'image/hen2.gif');
    }
    if (x >= 20){
      document.getElementById("b"+typeBox).setAttribute('src', 'image/hen.gif');
    }
}

function change(id){
  var check = document.getElementById(id).getAttribute('grow');
  var num = document.getElementById(id);
  var x = Number(id[1]);
  if (check >= 100){
    money += 500;
    num.setAttribute('grow', 0);
  }
  else if (CheckFood == 1 && check != 0 && check < 90){
      CheckFood = 0;
      num.setAttribute('grow', Number(num.innerHTML) + 10);
    }
    CheckFood = 0;
}

function food(){
  if (money >= 20 && CheckFood == 0){
    money -= 20;
    CheckFood = 1;
  }
}

function Shop(){
  if (money >= 100){
    money -= 100;
    shop = 1;
  }
}

function Egg(id){
  id = id[1];
  money += 50;
  document.getElementById("e"+id).setAttribute('size', 'a');
  egg[id-1] = 0;
}

function walk(){
  var numA = Math.floor(Math.random()*8+1);
  var numC = "b"+numA;
  var chick = document.getElementById(numC);
  var num = Math.floor(Math.random()*5);
  var walking = 50*(num == 1 || num == 2) + -50*(num == 3 || num == 4);
  if (chick.getAttribute('grow') >= 1){
    var numR = Math.floor(Math.random()*3);
    var x = chick.getAttribute('x');
    var y = chick.getAttribute('y');
    x = Number(x);
    y = Number(y);
    x += walking*(numR%2 == 0)*(x+walking > -50 && x+walking < 1200);
    y += walking*(numR%2 == 1)*(y+walking > -50 && y+walking < 400);
    chick.style.left = x + "px";
    chick.style.top = y + "px";
    chick.setAttribute('x', x);
    chick.setAttribute('y', y);
  }
}

function start(){
  Enemy[3] += 50;
  Enemy[2] = Enemy[3];
  Enemy[1] = 0;
  document.querySelector("#enemy").setAttribute('size','a');
  Enemy[0] = Math.floor(Math.random() * 10)+90;
}

function enemyTime(){
  enemyCount++;
  var shot = Math.floor(Math.random() * 10);
  var chick = document.getElementById("b"+shot);
  if (chick.getAttribute('grow') > 0 && shot <= 8 && enemyCount >= 7){
    enemyCount = 0;
    chicken[shot-1] = 0;
    document.getElementById("enemy").style.left = chick.getAttribute('x') + "px";
    document.getElementById("enemy").style.top = chick.getAttribute('y') + "px";
    document.getElementById("b"+shot).setAttribute('grow', 0);
    document.getElementById("b"+shot).setAttribute('size', 'a');
    document.getElementById("b"+shot).setAttribute('src', 'image/chick_flip.gif');
  }
}

function kill(){
  if (document.querySelector("#enemy").getAttribute('size') == "c"){
    Enemy[2] -= 20*gun;
  }
  if (Enemy[2] <= 0){
    start();
  }
}

function gunMan(){
  if (money >= 200){
    gun++;
    money -= 200;
    document.getElementById("gun").innerHTML = "Lv."+gun;
  }
}

game = setInterval(gameplay, 300);

farm.addEventListener("click", spon);
