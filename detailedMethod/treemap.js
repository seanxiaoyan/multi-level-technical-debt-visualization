const fs = require('fs');
const csv=require('csvtojson');
const ipc = require('electron').ipcRenderer;

let data_json;

function drawChart() {
  var x = document.getElementById("select").value;
  if(x=="1"){
    try {
      data_json = fs.readFileSync('./detailedMethod/data-all.json', 'utf8');
  } catch (err) {
    console.error(err);
  }}
  else if(x=="2"){
      try {
        data_json = fs.readFileSync('./detailedMethod/data-long-method.json', 'utf8');
      } catch (err) {
        console.error(err);
      }
  }
  else if(x=="3"){
      try {
        data_json = fs.readFileSync('./detailedMethod/data-long-parameter-list.json', 'utf8');
      } catch (err) {
        console.error(err);
      }
  }
  else if(x=="4"){
    try {
      data_json = fs.readFileSync('./detailedMethod/data-shotgun-surgery.json', 'utf8');
    } catch (err) {
      console.error(err);
    }
  }
  else{
    try {
      data_json = fs.readFileSync('./detailedMethod/data-brain-method.json', 'utf8');
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
