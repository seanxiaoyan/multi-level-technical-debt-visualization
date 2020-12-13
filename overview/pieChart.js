const fs = require('fs');
function drawChart() {
  let smell_json_str;
  try {
     smell_json_str = fs.readFileSync('./overview/smell-all.json', 'utf8');
  } catch (err) {
    console.error(err)
  }
  smell_jsonObj = JSON.parse(smell_json_str);
  let dataArray = [
    ['Smell Name', 'Count'],
    ['packageLevel', 0],
    ['classLevel', 0],
    ['methodLevel', 0]
  ]

  for (row of smell_jsonObj){
    // sum package level smell
    if (row.Unstable_Dependency) {dataArray[1][1] += parseInt(row.Unstable_Dependency);};
    if (row.Package_Cyclic_Dependency) {dataArray[1][1] += parseInt(row.Package_Cyclic_Dependency);};

    // sum class level smell
    if (row.God_Class) {dataArray[2][1] += parseInt(row.God_Class);};
    if (row.Data_Class) {dataArray[2][1] += parseInt(row.Data_Class);};
    if (row.Lazy_Class) {dataArray[2][1] += parseInt(row.Lazy_Class);};
    if (row.Refused_Request) {dataArray[2][1] += parseInt(row.Refused_Request);};
    if (row.Brain_Class) {dataArray[2][1] += parseInt(row.Brain_Class);};
    if (row.Unhealthy_Inheritance_Hierarchy) {dataArray[2][1] += parseInt(row.Unhealthy_Inheritance_Hierarchy);};
    if (row.Hub_Like_Dependency) {dataArray[2][1] += parseInt(row.Hub_Like_Dependency);};
    if (row.Large_Class) {dataArray[2][1] += parseInt(row.Large_Class);};
    if (row.Complex_Class) {dataArray[2][1] += parseInt(row.Complex_Class);};

    // sum method level smell
    if (row.Brain_Method) {dataArray[3][1] += parseInt(row.Brain_Method);};
    if (row.Feature_Envy) {dataArray[3][1] += parseInt(row.Feature_Envy);};
    if (row.Long_Parameter_List) {dataArray[3][1] += parseInt(row.Long_Parameter_List);};
    if (row.Shotgun_Surgery) {dataArray[3][1] += parseInt(row.Shotgun_Surgery);};
    if (row.Long_Method) {dataArray[3][1] += parseInt(row.Long_Method);};
  }

  console.log(dataArray)
  let data = google.visualization.arrayToDataTable(dataArray);
  let options = {

  };
  let chart = new google.visualization.PieChart(document.getElementById('piechart'));

  chart.draw(data, options);

  // document.getElementById('piechart').setAttribute("style", "display: unset;");
}