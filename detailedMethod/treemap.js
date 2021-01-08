const fs = require('fs');
const csv=require('csvtojson');
const ipc = require('electron').ipcRenderer;

let data_json;
try {
   data_json = fs.readFileSync('./detailedMethod/data.json', 'utf8');
} catch (err) {
  console.error(err)
}
dataArray = JSON.parse(data_json);


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
        return size;
      }

};
