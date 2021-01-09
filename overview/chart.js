const fs = require('fs');
let smell_json_str;
try {
   smell_json_str = fs.readFileSync('./overview/smell-all.json', 'utf8');
} catch (err) {
  console.error(err)
}

let pieChart_data_json;
try {
   pieChart_data_json = fs.readFileSync('./overview/pieChartData.json', 'utf8');
} catch (err) {
  console.error(err)
}
let pieChartArray = JSON.parse(pieChart_data_json);

let barChart_data_json;
try {
   barChart_data_json = fs.readFileSync('./overview/barChartData.json', 'utf8');
} catch (err) {
  console.error(err)
}
let barChartArray = JSON.parse(barChart_data_json);
barChartArray[0].push({ role: "style" })




// smell_jsonObj = JSON.parse(smell_json_str);


// let barChartArray = [
//   ["Smell Name", "Count", { role: "style" } ],
//   ["Package Cyclic Dependency", 0, "#3366cc"],
//   ["Unstable Dependency", 0, "#3366cc"],
//   ["God Class", 0, "#dc3912"],
//   ["Data Class", 0, "#dc3912"],
//   ["Lazy Class", 0, "#dc3912"],
//   ["Refused Request", 0, "#dc3912"],
//   ["Brain Class", 0, "#dc3912"],
//   ["Unhealthy Inheritance", 0, "#dc3912"],
//   ["Hub Like Dependency", 0, "#dc3912"],
//   ["Large Class", 0, "#dc3912"],
//   ["Complex Class", 0, "#dc3912"],
//   ["Class Cyclic Dependency", 0, "#dc3912"],
//   ["Feature Envy", 0, "#dc3912"],
//   ["Brain Method", 0, "#ff9900"],
//   ["Long Parameter List", 0, "#ff9900"],
//   ["Shotgun Surgery", 0, "#ff9900"],
//   ["Long Method", 0, "#ff9900"]
  
// ]

// for (row of smell_jsonObj){
//   // sum package level smell
//   if (row.Unstable_Dependency) {
    
//     barChartArray[2][1] += parseInt(row.Unstable_Dependency);
//   };
//   if (row.Package_Cyclic_Dependency) {
    
//     barChartArray[1][1] += parseInt(row.Package_Cyclic_Dependency);
//   };

//   // sum class level smell
//   if (row.God_Class) {
//     barChartArray[3][1] += parseInt(row.God_Class);
//   };
//   if (row.Data_Class) {
//     barChartArray[4][1] += parseInt(row.Data_Class);
//   };
//   if (row.Lazy_Class) {
//     barChartArray[5][1] += parseInt(row.Lazy_Class);
//   };
//   if (row.Refused_Request) {
//     barChartArray[6][1] += parseInt(row.Refused_Request);
//   };
//   if (row.Brain_Class) {
//     barChartArray[7][1] += parseInt(row.Brain_Class);
//   };
//   if (row.Unhealthy_Inheritance_Hierarchy) {
//     barChartArray[8][1] += parseInt(row.Unhealthy_Inheritance_Hierarchy);
//   };
//   if (row.Hub_Like_Dependency) {
//     barChartArray[9][1] += parseInt(row.Hub_Like_Dependency);
//   };
//   if (row.Large_Class) {
//     barChartArray[10][1] += parseInt(row.Large_Class);
//   };
//   if (row.Complex_Class) {
//     barChartArray[11][1] += parseInt(row.Complex_Class);
//   };
//   if (row.Class_Cyclic_Dependency) {
//     barChartArray[12][1] += parseInt(row.Class_Cyclic_Dependency);
//   };

//   if (row.Feature_Envy) {
//     barChartArray[13][1] += parseInt(row.Feature_Envy);
//   };
//   // sum method level smell
//   if (row.Brain_Method) {
//     barChartArray[14][1] == parseInt(row.Brain_Method);
//   };

//   if (row.Long_Parameter_List) {
//     barChartArray[15][1] += parseInt(row.Long_Parameter_List);
//   };
//   if (row.Shotgun_Surgery) {
//     barChartArray[16][1] += parseInt(row.Shotgun_Surgery);
//   };
//   if (row.Long_Method) {
//     barChartArray[17][1] += parseInt(row.Long_Method);
//   };
// }

function drawPieChart() {
  console.log(pieChartArray)
  let data = google.visualization.arrayToDataTable(pieChartArray);
  let options = {
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
                   2]);
  var options = {
    width: 700,
    height: 500,
    bar: {groupWidth: "95%"},
    legend: { position: "none" },
  };
  var chart = new google.visualization.BarChart(document.getElementById("barchart"));
  chart.draw(view, options);
};
