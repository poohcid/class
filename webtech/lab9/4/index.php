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
        <?php
        $url = "http://10.0.15.12/lab9/restapis/nobleprize100";
        $myJson = json_decode(file_get_contents($url));
        ?>
        <form action="" method="POST">
            <label for="">เลือกปี : </label>
            <select name="year">
                <option value="2010" <?php if(isset($_POST['submit'])){if($_POST['year'] == '2010'){echo "selected";}} ?>>2010</option>
                <option value="2011" <?php if(isset($_POST['submit'])){if($_POST['year'] == '2011'){echo "selected";}} ?>>2011</option>
                <option value="2012" <?php if(isset($_POST['submit'])){if($_POST['year'] == '2012'){echo "selected";}} ?>>2012</option>
                <option value="2013" <?php if(isset($_POST['submit'])){if($_POST['year'] == '2013'){echo "selected";}} ?>>2013</option>
                <option value="2014" <?php if(isset($_POST['submit'])){if($_POST['year'] == '2014'){echo "selected";}} ?>>2014</option>
                <option value="2015" <?php if(isset($_POST['submit'])){if($_POST['year'] == '2015'){echo "selected";}} ?>>2015</option>
                <option value="2016" <?php if(isset($_POST['submit'])){if($_POST['year'] == '2016'){echo "selected";}} ?>>2016</option>
                <option value="2017" <?php if(isset($_POST['submit'])){if($_POST['year'] == '2017'){echo "selected";}} ?>>2017</option>
                <option value="2018" <?php if(isset($_POST['submit'])){if($_POST['year'] == '2018'){echo "selected";}} ?>>2018</option>
            </select>
            <button type="submit" name="submit">แสดง</button>
        </form>
    </div>
    <div class="container">
        <table class="table table-bordered">
            <?php
            if (isset($_POST['submit'])) {
                $year = $_POST['year'];
                $color = array('table-active', '');
                $count = 2;
                echo "<tr><th class='col table-dark' colspan='6'><h2 class='text-center'>{$year}</h2></th></tr>";
                echo "<tr><th class='text-center table-dark' rowspan='2'>category</th>";
                echo "<th colspan='4' class='text-center table-dark'>laureates</th></tr>";
                echo "<tr><th class='text-center table-dark'>id</th>
                <th class='text-center table-dark'>firstname</th>
                <th class='text-center table-dark'>surname</th>
                <th class='text-center table-dark'>motivation</th><tr>";
                foreach ($myJson as $movie){
                    if ($movie->year == $year){
                        $size = count($movie->laureates);
                        $count++;
                        echo "<tr><td rowspan='{$size}' class='".$color[$count%2]."'>{$movie->category}</td>";
                        $arrayId = $movie->laureates;
                        echo "<td class='".$color[$count%2]."'>"
                        .$arrayId[0]->id."</td><td class='".$color[$count%2]."'>"
                        .$arrayId[0]->firstname."</td><td class='".$color[$count%2]."'>"
                        .$arrayId[0]->surname."</td><td class='".$color[$count%2]."'>"
                        .$arrayId[0]->motivation."</td></tr>";
                        array_shift($arrayId);
                        foreach ($arrayId as $id){
                            echo "<tr><td class='".$color[$count%2]."'>
                            {$id->id}</td><td class='".$color[$count%2]."'>
                            {$id->firstname}</td><td class='".$color[$count%2]."'>
                            {$id->surname}</td><td class='".$color[$count%2]."'>
                            {$id->motivation}</td></tr>";
                        }
                    }
                }
            }
            ?>
        </table>
    </div>
</body>

</html>