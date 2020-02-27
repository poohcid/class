<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
    <title>Document</title>
</head>
<body>
    <div class="container">
        <table class="table">
            <?php
            $url = "http://10.0.15.12/lab9/restapis/10countries";
            $myJson = json_decode(file_get_contents($url));

            foreach ($myJson as $contry){
                echo "<tr class='row'><td class='col-4'>";
                echo "<p>Name : <b>{$contry->name}</b></p>";
                echo "<p>Capital : {$contry->capital}</p>";
                echo "<p>Region : {$contry->region}</p>";
                echo "<p>Location : ".$contry->latlng[0]." ".$contry->latlng[1]."</p>";
                echo "<p>Border : ";
                foreach ($contry->borders as $border){
                    echo "{$border} ";
                }
                echo "</p></td><td class='col-8'><br>";
                echo "<img width='200px' class='img-Thumbnail' src='{$contry->flag}'>";
                echo "</td></tr>";
            }
            ?>
        </table>
    </div>
</body>
</html>