function check(){
    let myform = document.forms["myform"];
    let text = myform["idNumber"].value;
    if (isNaN(text)){
        alert("เลขบัตรใส่เป็นตัวเลขเท่านั้น")
        return false;
    }
    if (text.length < 13 || text.length == 0){
        alert("ใส่ให้ครบ 13 หลัก");
        return false;
    }

    let nameTitle = myform["title"].value;
    if (nameTitle == "คำนำหน้า"){
        alert("โปรดระบุคำนำหน้า");
        return false;
    }

    text = myform["name"].value;
    if (!(isNaN(text))){
        alert("ใส่ชื่อป็นตัวอักษรเท่านั้น")
        return false;
    }
    if (text.length < 2 || text.length > 20){
        alert("ความยาวชื่อต้องใส่ 2-20 ตัวอักษร");
        return false;
    }

    text = myform["lastname"].value;
    if (!(isNaN(text))){
        alert("ใส่นามสกุลเป็นตัวอักษรเท่านั้น")
        return false;
    }
    if (text.length < 2 || text.length > 20){
        alert("ความยาวนามสกุลต้องใส่ 2-20 ตัวอักษร");
        return false;
    }

    text = myform["address1"].value;
    if (text.length < 5){
        alert("ที่อยู่ต้องใส่มากกว่า 5 ตัวอักษร");
        return false;
    }

    text = myform["address2"].value;
    if (text.length < 5){
        alert("ที่อยู่ต้องใส่มากกว่า 5 ตัวอักษร");
        return false;
    }

    text = myform["ad1"].value;
    if (!(isNaN(text))){
        alert("ใส่ตำบลป็นตัวอักษรเท่านั้น")
        return false;
    }
    if (text.length < 2){
        alert("ความยาวต้องใส่ 2-20 ตัวอักษร");
        return false;
    }

    text = myform["ad2"].value;
    if (!(isNaN(text))){
        alert("ใส่อำเภอป็นตัวอักษรเท่านั้น")
        return false;
    }

    nameTitle = myform["ad3"].value;
    if (nameTitle == "โปรดระบุจังหวัด"){
        alert("โปรดระบุจังหวัด");
        return false;
    }

    text = myform["namepost"].value;
    if (isNaN(text)){
        alert("ใส่เลขรหัสเป็นตัวเลขเท่านั้น")
        return false;
    }
    if (text.length != 5){
        alert("ใส่ให้ครบ 5 หลัก");
        return false;
    }

    text = myform["namephone"].value;
    if (isNaN(text)){
        alert("ใส่เบอร์โทรเป็นตัวเลขเท่านั้น")
        return false;
    }
    if (text.length < 9 || text.length > 10){
        alert("ใส่ให้ครบ 9 - 10 หลัก");
        return false;
    }
}