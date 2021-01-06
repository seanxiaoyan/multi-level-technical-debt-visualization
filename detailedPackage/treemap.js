let dataArray = [
    ['Location', 'Parent', 'Market trade volume (size)', 'Market increase/decrease (color)'],
    ['Global',    null,                 0,                               0],
    ['A',   'Global',             0,                               0],
    ['B',   'Global',             0,                               0],
];


for (var n = 0; n < 100; n++) {
    dataArray.push([n.toString(),   'A',             1,                               0])
}
function drawChart() {
    var data = google.visualization.arrayToDataTable(dataArray);

    tree = new google.visualization.TreeMap(document.getElementById('chart_div'));

    tree.draw(data, {
      minColor: '#f00',
      midColor: '#ddd',
      maxColor: '#0d0',
      headerHeight: 15,
      fontColor: 'black',
      generateTooltip: showStaticTooltip
    });

    function showStaticTooltip(row, size, value) {
        return  '# of smells detected: ' +size;
      }

  }