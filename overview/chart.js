const fs = require('fs');

let pieChart_data_json;
try {
   pieChart_data_json = fs.readFileSync('./overview/pieChartData.json', 'utf8');
} catch (err) {
  console.error(err);
}
let pieChartArray = JSON.parse(pieChart_data_json);

let barChart_data_json;
try {
   barChart_data_json = fs.readFileSync('./overview/barChartData.json', 'utf8');
} catch (err) {
  console.error(err);
}
let barChartArray = JSON.parse(barChart_data_json);
barChartArray[0].push({ role: "style" })

let data_json;
try {
   data_json = fs.readFileSync('./detailedPackage/data-all.json', 'utf8');
} catch (err) {
  console.error(err)
}
dataArray = JSON.parse(data_json);


function drawPieChart() {

  document.getElementById("project-name").innerHTML = dataArray[1][0].toString('utf8');
  document.getElementById("total-smell").innerHTML = (pieChartArray[1][1]+pieChartArray[2][1]+pieChartArray[3][1]).toLocaleString();
  document.getElementById("smell-package").innerHTML =  pieChartArray[1][1].toLocaleString();
  document.getElementById("smell-class").innerHTML = pieChartArray[2][1].toLocaleString();
  document.getElementById("smell-method").innerHTML = pieChartArray[3][1].toLocaleString();
  let data = google.visualization.arrayToDataTable(pieChartArray);
  let options = {
    sliceVisibilityThreshold: 0.001,
    colors: ['#803C05', '#D5BB9E','#178CCB']
  };
  let chart = new google.visualization.PieChart(document.getElementById('piechart'));
  chart.draw(data, options);
}

function drawBarChart() {
  var data = google.visualization.arrayToDataTable(barChartArray);
  var view = new google.visualization.DataView(data);
  view.setColumns([0, 1,
                   { calc: "stringify",
                     sourceColumn: 1,
                     type: "string",
                     role: "annotation" },
                     2
                   ]);
  var options = {
    annotations: {
      textStyle: {
        // The color of the text.
        color: 'cyan',
        fontSize:20
      }
    },
    width: 1000,
    height: 750,
    bar: {groupWidth: "95%"},
    legend: { position: "none" },
  };
  var chart = new google.visualization.BarChart(document.getElementById("barchart"));
  chart.draw(view, options);
};
