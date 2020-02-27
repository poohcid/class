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
    <div class="container-fluid">
        <table class="table table-striped">
            <?php
            $url = "http://10.0.15.12/lab9/restapis/movies90";
            $response = file_get_contents($url);
            $myJson = json_decode($response);

            $count = 1;
            
            foreach ($myJson as $i) {
                echo "<tr><td>";
                echo "<h3>{$count}. {$i->title} ({$i->year})</h3>";
                echo "<h4>cast</h4><h5><ul>";
                foreach ($i->cast as $j) {
                    echo "<li>{$j}</li>";
                }
                echo "</ul></h5>";
                echo "<h5>genres : ".$i->genres[0];
                for ($j=1; $j < count($i->genres); $j++){
                    echo ", ".$i->genres[$j];
                }
                echo "</h5></td></tr>";
                $count++;
            }
            ?>
        </table>
    </div>
</body>

</html>