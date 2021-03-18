const fs = require('fs');
const csv=require('csvtojson');
const ipc = require('electron').ipcRenderer;
const path = require('path');

let data_json;


function drawChart() {
    var x = document.getElementById("select").value;
    if(x=="1"){
      try {
        let pathDataAll = path.join(__dirname,'data-all.json');
        data_json = fs.readFileSync(pathDataAll, 'utf8');
    } catch (err) {
      console.error(err);
    }}
    else if(x=="2"){
        try {
          let pathDataUD = path.join(__dirname,'data-unstable-dependency.json');
          data_json = fs.readFileSync(pathDataUD, 'utf8');
        } catch (err) {
          console.error(err);
        }
    }
    else{
        try {
          let pathDataCD = path.join(__dirname,'data-cyclic-dependency.json');
          data_json = fs.readFileSync(pathDataCD, 'utf8');
        } catch (err) {
          console.error(err);
        }
    }
    let dataArray = JSON.parse(data_json);
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
