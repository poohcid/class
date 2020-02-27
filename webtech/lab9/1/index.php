<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
    <link href="https://fonts.googleapis.com/css?family=Mitr&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
    <title>Document</title>
</head>

<body>
    <h1>Currency Converter</h1>
    <form action="" method="POST">
        <label>Form : </label>
        <select name="type1">
            <option value="THB" <?php if(isset($_POST['submit'])){if($_POST['type1'] == 'THB'){echo "selected";}} ?> >THB</option>
            <option value="JPY" <?php if(isset($_POST['submit'])){if($_POST['type1'] == 'JPY'){echo "selected";}} ?>>JPY</option>
            <option value="CNY" <?php if(isset($_POST['submit'])){if($_POST['type1'] == 'CNY'){echo "selected";}} ?>>CNY</option>
            <option value="SGD" <?php if(isset($_POST['submit'])){if($_POST['type1'] == 'SGD'){echo "selected";}} ?>>SGD</option>
            <option value="USD" <?php if(isset($_POST['submit'])){if($_POST['type1'] == 'USD'){echo "selected";}} ?>>USD</option>
        </select>
        <input type="text" name="num1" value="<?php if(isset($_POST['submit'])){echo $_POST['num1'];}?>"/><br>
        <label>To : </label>
        <select name="type2">
            <option value="THB" <?php if(isset($_POST['submit'])){if($_POST['type2'] == 'THB'){echo "selected";}} ?>>THB</option>
            <option value="JPY" <?php if(isset($_POST['submit'])){if($_POST['type2'] == 'JPY'){echo "selected";}} ?>>JPY</option>
            <option value="CNY" <?php if(isset($_POST['submit'])){if($_POST['type2'] == 'CNY'){echo "selected";}} ?>>CNY</option>
            <option value="SGD" <?php if(isset($_POST['submit'])){if($_POST['type2'] == 'SGD'){echo "selected";}} ?>>SGD</option>
            <option value="USD" <?php if(isset($_POST['submit'])){if($_POST['type2'] == 'USD'){echo "selected";}} ?>>USD</option>
        </select>
        <?php
        if (isset($_POST['submit'])) {
            $url = "http://10.0.15.12/lab9/restapis/latest";
            $response = file_get_contents($url);
            $result = json_decode($response);

            $type1 = $_POST['type1'];
            $num1 = intval($_POST['num1']);
            $type2 = $_POST['type2'];
            $num2 = $num1/($result->rates->$type1)*($result->rates->$type2);
            $num2 = round($num2, 2);
        }
        ?>
        <input type="text" name="num2" value="<?php if (isset($_POST['submit'])){echo $num2;}?>"><br><br>
        <button type="submit" name="submit">Convert</button><br><br>
    </form>
</body>

</html>