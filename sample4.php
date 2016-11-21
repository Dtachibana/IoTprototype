<html>
  <head>
    <!--Load the AJAX API-->
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">

      // Load the Visualization API and the corechart package.
      google.charts.load('current', {'packages':['corechart']});

      // Set a callback to run when the Google Visualization API is loaded.
      google.charts.setOnLoadCallback(drawChart);

      // Callback that creates and populates a data table,
      // instantiates the pie chart, passes in the data and
      // draws it.

      function drawChart() {

        // Create the data table.
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Topping');
        data.addColumn('number', 'Slices');
        data.addRows([

    <?php
      $pdo = new PDO("mysql:dbname=logging;host=localhost", "root", "choooh1031");
      $st = $pdo->query("SELECT * FROM pressure");
      while ($row = $st->fetch()) {
          if ($i != 0) {
              $drawScript .=", ['" . $row['date'] . "', " . (int)$row['value'] . "]";
          } else {
              $drawScript .= "['" . $row['date'] . "', " . (int)$row['value'] . "]";
              // 一つ目の項目は 前に コンマ がいらないのと要素を入れる必要があるため
          }
          $i++;
      }

    ?>
    <?php
        $mash="['Mushrooms', 3],";
?>
//          <?=$mash?>
['日付', '値'],
          <?=$drawScript?>

//['2016-11-10 04:11:31', 0], ['2016-11-10 04:11:33', 0], ['2016-11-10 04:15:52', 0], ['2016-11-10 04:15:54', 0], ['2016-11-10 04:21:09', 0], ['2016-11-10 04:21:29', 0], ['2016-11-10 04:22:17', 0], ['2016-11-10 04:22:19', 0], ['2016-11-10 04:22:21', 0], ['2016-11-10 04:27:41', 958], ['2016-11-10 04:27:43', 977], ['2016-11-11 02:52:19', 935], ['2016-11-11 02:52:21', 953], ['2016-11-11 02:52:22', 962],
//['2016-11-10 11:00:00', 1], ['2016-11-12 11:00:00', 2], ['2116-11-10 11:00:00', 962],
//['Mushrooms', 3],
//          ['Onions', 1],
//          ['Olives', 1],
//          ['Zucchini', 1],
//          ['Pepperoni', 2]
        ]);

        // Set chart options
        var options = {'title':'How Much Pizza I Ate Last Night',
                       'width':2000,
                       'height':1500};

        // Instantiate and draw our chart, passing in some options.
//        var chart = new google.visualization.PieChart(document.getElementById('chart_div'));
        var chart = new google.visualization.AreaChart(document.getElementById('chart_div'));
        chart.draw(data, options);
      }
    </script>
  </head>

  <body>
    <!--Div that will hold the pie chart-->

    <div id="chart_div"></div>
  </body>
</html>