<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="style.css">
    <link href="https://fonts.googleapis.com/css?family=Kanit&display=swap" rel="stylesheet">
    <title>Document</title>
</head>
<body>
    <?php
        $arr = array("idNumber", "name", "lastname", "add1", "add2", "add3", "code", "number");
        $names = array("หมายเลขบัตรประชาชน", "ชื่อ", "นามสกุล", "ที่อยู่", "อำเภอ เขต", "จังหวัด", "รหัสไปรษณีย์", "เบอร์โทรศัพท์");
        echo "<table><tr><th>ลำดับ</th><th>รายการ</th><th>ข้อมูล</th></tr>";

        for($i=0; $i < 8; $i++){
            $var = $_POST[$arr[$i]];
            echo "<tr><td>$i</td><td>".($names[$i])."</td><td><p ";
            if (strlen($var) < 5){
                echo "style='color: red; '";
            }
            echo ">$var</p></td></tr>";
        }
        echo "</table>";
    ?>
</body>
</html>