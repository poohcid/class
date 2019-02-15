score = 0;
cd = 10;
setTimeout(function(){
  the_vote.setAttribute('onclick','');
},10000);
setInterval(function(){
  if (cd>0){
      cd--;
      the_countdown.innerText = cd;
  }
},1000);
function updateScore(){
  the_score.innerText = score;
}
function vote(){
  score++;
  updateScore();
}
setInterval(function(){
  the_vote.click()
},0.01)