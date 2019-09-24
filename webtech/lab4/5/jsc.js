let sizeText = 24;
let colorList = ["red", "coral", "limegreen", "black"];

function addText(add){
    let text = document.getElementById("text");
    sizeText += add;
    sizeText = Math.max(sizeText, 0);
    text.style.fontSize = ""+(sizeText)+"pt";
}

function changeC(add){
    let textColor;
    if (!add){
        textColor = colorList.pop();
        colorList.unshift(textColor);
    }

    else{
        textColor = colorList.shift();
        colorList.push(textColor);
    }

    document.getElementById("text").style.color = colorList[3];
}