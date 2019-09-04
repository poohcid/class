function change(){
    let p1 = document.getElementById("p1").src;
    let p2 = document.getElementById("p2").src;
    let p3 = document.getElementById("p3").src;
    let p4 = document.getElementById("p4").src;

    document.getElementById("p1").src = p3;
    document.getElementById("p2").src = p1;
    document.getElementById("p3").src = p4;
    document.getElementById("p4").src = p2;
}