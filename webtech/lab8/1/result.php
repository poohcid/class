<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="style.css">
    <title>Document</title>
</head>

<body>
    <?php
    $number = $_POST['num'];
    echo "<h1>ตารางสูตรคูณแม่ " . $number."</h1>";
    $number = intval($number);
    echo "<table>";
    for ($i = 1; $i < 13; $i++){
        echo "<tr>";
        echo "<td><pre>".$number."    x    ".$i." = ".($number*$i)."</pre></td>";
        echo "</tr>";
    }
    echo "</table>"
    ?>
</body>

</html>