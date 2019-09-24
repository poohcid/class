function fruit(text){
    let box = document.getElementById("show");
    let x = document.createElement("img");
    x.src = text+".png";
    box.appendChild(x);
}