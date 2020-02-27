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
    echo "<h1>June 2019</h1>";
    echo "<table><tr>";
    echo "<th>Su</th><th>Mo</th><th>Tu</th><th>We</th><th>th</th><th>Fr</th><th>Sa</th></tr>";
    $count = -5;
    while ($count <= 30){
        echo "<tr>";
        for ($i = 0; $i < 7; $i++){
            if ($count >= 1 && $count < 31){
                echo "<td>".($count++)."</td>";
            }
            else{
                $count++;
                echo "<td></td>";
            }
        }
        echo "</tr>";
    }
    echo "</table>";
    ?>
</body>
</html>