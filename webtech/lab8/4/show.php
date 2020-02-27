<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
    <!-- jQuery library -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <!-- Latest compiled JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
    <link href="https://fonts.googleapis.com/css?family=Kanit&display=swap" rel="stylesheet">
    <title>Document</title>
</head>
<body>
    <?php
        $arr = array("idNumber", "name", "lastname", "add1", "add2", "add3", "code", "number");
        $names = array("หมายเลขบัตรประชาชน", "ชื่อ", "นามสกุล", "ที่อยู่", "อำเภอ เขต", "จังหวัด", "รหัสไปรษณีย์", "เบอร์โทรศัพท์");
        $asar = array();
        for ($i=0; $i < count($names); $i++){
            $asar[$names[$i]] = $_POST[$arr[$i]];
        }
        echo "<div class='container-fluid' ><table class='table table-striped' ><tr><th>ลำดับ</th><th>รายการ</th><th>ข้อมูล</th></tr>";
        $count = 0;
        foreach($asar as $key => $var){
            $count++;
            echo "<tr><td>$count</td><td>$key</td><td><p ";
            if (strlen($var) < 5){
                echo "style='color: red; '";
            }
            echo ">$var</p></td></tr>";
        }
        echo "</table></div>";
    ?>
</body>
</html>