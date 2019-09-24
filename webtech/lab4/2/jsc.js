function calcu(){
    let num1 = Number(document.getElementById("form1").value);
    let num2 = Number(document.getElementById("form2").value);
    let result = num1+num2;
    document.getElementById("result").innerHTML = "Result : "+result;

    let x = document.createElement("p");
    let y = document.createTextNode(num1+" + "+num2+" = "+result);
    x.appendChild(y);
    document.body.appendChild(x);
}