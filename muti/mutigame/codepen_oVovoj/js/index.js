var CheckFood=0;
var CountFood=[0, 0, 0, 0, 0, 0, 0, 0];
var Chick = new Array();
setInterval(function(){
    var x = 0;
    var add=1;
    var typeBox = Math.floor(Math.random()*9);
    x = document.getElementById("b"+typeBox).innerHTML;
    x = Number(x);
    var In = Number(typeBox-1);
    document.getElementById("score").innerHTML = typeBox;
    if (CountFood[In] > 0){
      add += 3;
      CountFood[In]--;
    }
    if (x != 0 && x < 100){
        x += add;
        document.getElementById("b"+typeBox).innerHTML = x;
    }
    document.getElementById("bord").innerHTML = CountFood;
}, 300);

function change(id){
  var check = document.getElementById(id).innerHTML;
  var num = document.getElementById(id);
  var x = id[1];
  if (check == 0 && CheckFood == 0){
    num.innerHTML = 1;
    num.style.backgroundColor = "red";
    Chick[Chick.length] = id[1];
  }
  else if (CheckFood == 1 && check != 0 && check < 90){
      CheckFood = 0;
      num.innerHTML = Number(num.innerHTML) + 10;
    }
    CheckFood = 0;
}

function food(){
  CheckFood = 1;
  alert(CheckFood);
}

function allFood(){
  if (CheckFood == 1){
    for (var i=0; i < 8; i++)
      CountFood[i] += Math.floor(Math.random()*4+1);
  }
    CheckFood = 0;
}