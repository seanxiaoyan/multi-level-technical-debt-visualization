google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {

  var data = google.visualization.arrayToDataTable([
    ['Smell Name', 'Count'],
    ['packageLevel',  1100],
    ['classLevel',    222],
    ['methodLevel',  900]
  ]);

  var options = {
    
  };

  var chart = new google.visualization.PieChart(document.getElementById('piechart'));
  var chart2 = new google.visualization.PieChart(document.getElementById('piechart2'));

  chart.draw(data, options);
  chart2.draw(data, options);

  // document.getElementById('piechart').setAttribute("style", "display: unset;");
}