

function Chess(){
    let tb = document.createElement("table");
    tb.className = "table-bordered border-secondary border-3";
    let tr, td;

    for (let i=0; i < 8; i++){
        tr = tb.insertRow(-1);
        for (let j=0; j < 8; j++){
            td  = tr.insertCell(-1);
            if ((i+j)%2 == 0){
                td.style = "background-color: #222222";
                console.log(i);
            }
            else{
                td.style = "background-color: antiquewhite";
            }
        }
    }
    document.body.appendChild(tb);
}

Chess();
