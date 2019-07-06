var listGrass = [];
var listWash = [3, 4, 5];
var time = 0;
var score = 0;
var diff = 20;
var count = 500;
var ang = 0;
var hpwash = 3;
var bar = 0;
var game;
var speed = 700;
var countWash = 10;

function grass(val){
  var stat = document.getElementById("g"+val).getAttribute('size');
  if (stat == "a"){
    document.getElementById("g"+val).setAttribute('size', "b");
    listGrass[listGrass.length] = val;
  }
}

function wash(val){
  bowl = document.getElementById("w"+val);
  if (bowl.getAttribute('size') == "a"){
    var hp = Number(bowl.getAttribute('hp'));
    hp -= 1;
    bowl.setAttribute('hp', hp);
    if (bowl.getAttribute('hp') <= 0){
      bowl.setAttribute('size', "b");
      listWash[listWash.length] = val;
    }
  }
}

function spon(){
  time += 1;
  if (bar >= 400){
    clearInterval(game);
    window.location.href = "#popup1";
  }
  if (time%20 == 0){
    score += 120;
    document.getElementById("score").innerHTML = score;
  }
  if (time%2 == 0 && listGrass.length > 0){
    var num = listGrass[Math.floor(Math.random()*listGrass.length)];
    listGrass.splice(listGrass.indexOf(num), 1);
    document.getElementById("g"+num).setAttribute('size', "a");
  }
  if (time%countWash == 0 && listWash.length > 0){
    var num = listWash[Math.floor(Math.random()*listWash.length)];
    listWash.splice(listWash.indexOf(num), 1);
    document.getElementById("w"+num).setAttribute('size', "a");
    document.getElementById("w"+num).setAttribute('hp', hpwash);
  }
  if (listWash.length < 3 || listGrass.length < 6)
    ang += 1;
  if (ang >= 5){
    bar += 50;
    document.getElementById("hp_bar").style.width = bar+"px";
    ang = 0;
  }
  if (time%40 == 0)
    hpwash += 3;
  if (time%30 == 0)
    speed -= 300;
}

function regame(){
  window.location.href = "#";
  time = 0;
  score = 0;
  diff = 20;
  count = 500;
  ang = 0;
  hpwash = 3;
  bar = 0;
  speed = 700;
  document.getElementById("hp_bar").style.width = bar+"px";
  document.getElementById("score").innerHTML = score;
  if (document.getElementById("score").innerHTML == "0")
    game = setInterval(spon, speed);
}

game = setInterval(spon, speed);