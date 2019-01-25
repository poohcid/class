<?php
  if( !isset($_POST['name']) ) {
    header("location: ./index.php");
  }
?>

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>Trolley | list foods</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
  <link rel="stylesheet" type="text/css" href="style.css" />
  <table id ="t01" style="width:60%">
    <tbody>
  <h1>Trolley</h1>
    <h2>Shipping Address</h2>
    <p id="p01">
  <?php
    $name = $_POST['name'];
    echo "Name:", $name;
  ?>
</p>
    <table id ="t04" style="width:60%">
    <thead>
      <tr>
        <th>Name</th>
        <th>Price</th>
        <th>Quantity</th>
        <th>Total</th>
      </tr>
    </thead>
      <?php
        /*
         * intval('1') === int('1') in Python
         */
        $apple_quantity = intval($_POST['donut']);
        $pineapple_quantity = intval($_POST['hamberger']);
        $orange_quantity = intval($_POST['coke']);

        /*
         * isset($apple_quantity) à¹€à¸Šà¹‡à¸„à¸•à¸±à¸§à¹à¸›à¸£à¸§à¹ˆà¸²à¸¡à¸µà¸„à¹ˆà¸²à¸«à¸£à¸·à¸­à¹„à¸¡à¹ˆ
         */
        if (isset($apple_quantity) && $apple_quantity > 0) {
          $apple_total = $apple_quantity * 30.00;
          $free_d = floor($apple_quantity/5);
          $apple_quantity += $free_d;
          $apple_total = number_format($apple_total, 2, '.', ''); // number_format() à¸ˆà¸±à¸”à¸à¸²à¸£à¸—à¸¨à¸™à¸´à¸¢à¸¡
          echo "<tr>" .
               "<td>Donut</td>" .
               '<td class="price">30.00 Bath</td>' .
               "<td class=\"price\">$apple_quantity</td>" .
               "<td class=\"price\">$$apple_total</td>" .
               "</tr>";
        }

        if (isset($pineapple_quantity) && $pineapple_quantity > 0) {
          $pineapple_total = $pineapple_quantity * 40.00;
          $free_d = floor($pineapple_quantity/5);
          $pineapple_quantity += $free_d;
          $pineapple_total = number_format($pineapple_total, 2, '.', '');
          echo "<tr>" .
               "<td>Hamberger</td>" .
               '<td class="price">40.00 Bath</td>' .
               "<td class=\"price\">$pineapple_quantity</td>" .
               "<td class=\"price\">$$pineapple_total</td>" .
               "</tr>";
        }

        if (isset($orange_quantity) && $orange_quantity > 0) {
          $orange_total = $orange_quantity * 15.00;
          $free_d = floor($orange_quantity/5);
          $orange_quantity += $free_d;
          $orange_total = number_format($orange_total, 2, '.', '');
          echo "<tr>" .
               "<td>Coke</td>" .
               '<td class="price">15.00 Bath</td>' .
               "<td class=\"price\">$orange_quantity</td>" .
               "<td class=\"price\">$$orange_total</td>" .
               "</tr>";
        }
      ?>
    </table>
    </tbody>
    <h2 id="h01">
      <?php
      $total = $orange_total+$pineapple_total+$apple_total;
      echo "Your Total Price: ", " $total", "Bath";
      ?>
    </h2>
  <p id="p01">
    <b>many more: </b> <a href="https://www.wongnai.com/" target="_blank">link it</a> <br />
  </p>
</table>
</body>
</html>