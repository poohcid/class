var CheckFood=0;
var CountFood=[0, 0, 0, 0, 0, 0, 0, 0];
var Chicken = 1;
var egg = [0, 0, 0, 0, 0, 0, 0, 0];
var game;
var Enemy = [0, 0, 100, 50];
var EnemyR;
var money = 500;
var gun=20;
function grow(){
    var x = 0;
    var add=1;
    var typeBox = Math.floor(Math.random()*9);
    Enemy[1]++;
    if (Enemy[0] == Enemy[1]){
      clearInterval(game);
      document.querySelector("#enemy").setAttribute('set','c');
      EnemyR = setInterval(enemyTime, 1300);
    }
    x = document.getElementById("b"+typeBox).innerHTML;
    x = Number(x);
    var In = Number(typeBox-1);
    if (CountFood[In] > 0){
      add += 3;
      CountFood[In]--;
    }
    if (x != 0 && x < 100){
        x += add;
        document.getElementById("b"+typeBox).innerHTML = x;
    }
    if (x >= 40 && (Math.floor(Math.random() * 6) == 5)){
      egg[typeBox-1] = 1;
      document.getElementById("b"+typeBox).style.backgroundColor = "green";
    }
    document.getElementById("money").innerHTML = money;
}

function change(id){
  var check = document.getElementById(id).innerHTML;
  var num = document.getElementById(id);
  var x = Number(id[1]);
  if (check >= 100){
    money += 500;
    num.innerHTML = 0;
    num.style.backgroundColor = "white";
  }
  else if (check == 0 && CheckFood == 0 && money >= 100){
    money -= 100;
    num.innerHTML = 1;
    num.style.backgroundColor = "red";
    Chick++;
  }
  else if (CheckFood == 1 && check != 0 && check < 90){
      CheckFood = 0;
      num.innerHTML = Number(num.innerHTML) + 10;
    }
    CheckFood = 0;
  if (egg[x-1] == 1){
    money += 50;
    egg[x-1] = 0
    num.style.backgroundColor = "red";
  }
}

function food(){
  if (money >= 20 && CheckFood == 0){
    money -= 20
    CheckFood = 1;
  }
}

function allFood(){
  if (CheckFood == 1){
    for (var i=0; i < 8; i++)
      CountFood[i] += Math.floor(Math.random()*4+1);
  }
    CheckFood = 0;
}

function kill(){
  if (document.querySelector("#enemy").getAttribute('set') == "c"){
    Enemy[2] -= gun;
  }
}

function enemyTime(){
  var shot = Math.floor(Math.random() * 9);
  if (document.getElementById("b"+shot).innerHTML > 0){
    document.getElementById("b"+shot).innerHTML = 0;
    document.getElementById("b"+shot).style.backgroundColor = "white";
  }
  if (Enemy[2] <= 0){
    clearInterval(EnemyR);
    start();
  }
}

function gunMan(){
  if (money >= 200){
    gun += 20;
    money -= 200;
    document.getElementById("gun").innerHTML = gun;
  }
}

function start(){
  Enemy[3] += 50;
  Enemy[2] = Enemy[3];
  Enemy[1] = 0;
  document.querySelector("#enemy").setAttribute('set','a');
  Enemy[0] = Math.floor(Math.random() * 10)+90;
  game = setInterval(grow, 300);
}
start();