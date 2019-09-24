let count = 0;

function register(){
    count += 1;
    let table = document.getElementById("table1");
    let row = table.insertRow(-1);
    let cell, text;

    cell = row.insertCell(-1);
    cell.appendChild(document.createTextNode(count));

    cell = row.insertCell(-1);
    text = document.getElementById("idNum").value;
    cell.appendChild(document.createTextNode(text));

    cell = row.insertCell(-1);
    text = document.getElementById("name").value;
    cell.appendChild(document.createTextNode(text));

    cell = row.insertCell(-1);
    text = document.getElementById("lastName").value;
    cell.appendChild(document.createTextNode(text));
}