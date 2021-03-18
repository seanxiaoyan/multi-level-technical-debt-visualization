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
        let pathDataGC = path.join(__dirname,'data-god-class.json');
        data_json = fs.readFileSync(pathDataGC, 'utf8');
      } catch (err) {
        console.error(err);
      }
  }
  else if(x=="3"){
    try {
      let pathDataLC = path.join(__dirname,'data-lazy-class.json');
      data_json = fs.readFileSync(pathDataLC, 'utf8');
    } catch (err) {
      console.error(err);
    }
  }
  else if(x=="4"){
    try {
      let pathDataCC = path.join(__dirname,'data-complex-class.json');
      data_json = fs.readFileSync(pathDataCC, 'utf8');
    } catch (err) {
      console.error(err);
    }
  }
  else if(x=="5"){
    try {
      let pathDataLargeC = path.join(__dirname,'data-large-class.json');
      data_json = fs.readFileSync(pathDataLargeC, 'utf8');
    } catch (err) {
      console.error(err);
    }
  }
  else if(x=="6"){
    try {
      let pathDataRR = path.join(__dirname,'data-refused-request.json');
      data_json = fs.readFileSync(pathDataRR, 'utf8');
    } catch (err) {
      console.error(err);
    }
  }
  else if(x=="7"){
    try {
      let pathDataDC = path.join(__dirname,'data-data-class.json.json');
      data_json = fs.readFileSync(pathDataDC, 'utf8');
    } catch (err) {
      console.error(err);
    }
  }
  else if(x=="8"){
    try {
      let pathDataFC = path.join(__dirname,'data-feature-envy.json');
      data_json = fs.readFileSync(pathDataFC, 'utf8');
    } catch (err) {
      console.error(err);
    }
  }
  else if(x=="9"){
    try {
      let pathDataBC = path.join(__dirname,'data-brain-class.json');
      data_json = fs.readFileSync(pathDataBC, 'utf8');
    } catch (err) {
      console.error(err);
    }
  }
  else if(x=="10"){
    try {
      let pathDataHLD = path.join(__dirname,'data-hub-like-dependency.json');
      data_json = fs.readFileSync(pathDataHLD, 'utf8');
    } catch (err) {
      console.error(err);
    }
  }

  else{
    try {
      let pathDataCCD = path.join(__dirname,'data-class-cyclic-dependency.json');
      data_json = fs.readFileSync(pathDataCCD, 'utf8');
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
