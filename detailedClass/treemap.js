const fs = require('fs');
const csv=require('csvtojson');
const ipc = require('electron').ipcRenderer;

let data_json;

function drawChart() {
  var x = document.getElementById("select").value;
  if(x=="1"){
    try {
      data_json = fs.readFileSync('./detailedClass/data-all.json', 'utf8');
  } catch (err) {
    console.error(err);
  }}
  else if(x=="2"){
      try {
        data_json = fs.readFileSync('./detailedClass/data-god-class.json', 'utf8');
      } catch (err) {
        console.error(err);
      }
  }
  else if(x=="3"){
    try {
      data_json = fs.readFileSync('./detailedClass/data-lazy-class.json', 'utf8');
    } catch (err) {
      console.error(err);
    }
  }
  else if(x=="4"){
    try {
      data_json = fs.readFileSync('./detailedClass/data-complex-class.json', 'utf8');
    } catch (err) {
      console.error(err);
    }
  }
  else if(x=="5"){
    try {
      data_json = fs.readFileSync('./detailedClass/data-large-class.json', 'utf8');
    } catch (err) {
      console.error(err);
    }
  }
  else if(x=="6"){
    try {
      data_json = fs.readFileSync('./detailedClass/data-refused-request.json', 'utf8');
    } catch (err) {
      console.error(err);
    }
  }
  else if(x=="7"){
    try {
      data_json = fs.readFileSync('./detailedClass/data-data-class.json', 'utf8');
    } catch (err) {
      console.error(err);
    }
  }
  else if(x=="8"){
    try {
      data_json = fs.readFileSync('./detailedClass/data-feature-envy.json', 'utf8');
    } catch (err) {
      console.error(err);
    }
  }
  else if(x=="9"){
    try {
      data_json = fs.readFileSync('./detailedClass/data-brain-class.json', 'utf8');
    } catch (err) {
      console.error(err);
    }
  }
  else if(x=="10"){
    try {
      data_json = fs.readFileSync('./detailedClass/data-hub-like-dependency.json', 'utf8');
    } catch (err) {
      console.error(err);
    }
  }

  else{
    try {
      data_json = fs.readFileSync('./detailedClass/data-class-cyclic-dependency.json', 'utf8');
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
