
function drawChart() {
    let data = google.visualization.arrayToDataTable([
      ['Smell Name', 'Count'],
      ['packageLevel',  1100],
      ['classLevel',    222],
      ['methodLevel',  900]
    ]);
    let options = {

    };
    let chart = new google.visualization.PieChart(document.getElementById('piechart'));

    chart.draw(data, options);

    // document.getElementById('piechart').setAttribute("style", "display: unset;");
  }