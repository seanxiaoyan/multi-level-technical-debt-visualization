const { electron } = require('process');
const ipc = require('electron').ipcRenderer;
const fs = require('fs');
const {dialog} = require('electron').remote;
const csv=require('csvtojson');
const path = require('path');

let overviewReady = 0;
let detailedClassReady = 0;

function detectSmell(){
    //set config.ini for GetSmells
    // use folder selector to get project path
    let pathArray = dialog.showOpenDialogSync({
        properties: ['openDirectory']
    });
    let proj_path = pathArray[0];

    let pathSetconfig = path.join(__dirname,'preProcessing','setconfig.py');

    let process_config = require('child_process').spawn('python3', [pathSetconfig,proj_path]);

    process_config.on('close',(code)=>{
        console.log(`set config exited with ${code}`);
    });

    //set PYTHONPATH for GetSmells and Execute GetSmells
    let pathGetsmell = path.join(__dirname,'preProcessing','getsmell.sh');
    let process_detectsmell = require('child_process').exec(pathGetsmell);
    process_detectsmell.stdout.on('data',function(data){
        document.getElementById("progressBar").innerHTML = data.toString('utf8');
    });
          
    let projName;
    process_detectsmell.on('close',(code)=>{
            console.log(`set PYTHONPATH and execute GetSmells process exited with code ${code}`);
            
            let splits = proj_path.split('/');
            let len = splits.length;
            projName = splits[len-1];
            
            const csvFilePath_overview = path.join(__dirname,'GetSmells','getsmells-output','smells',projName+'.csv');

            // if smell detected, then proceed to process csv files
            if (fs.existsSync(csvFilePath_overview)){
                csv()
                .fromFile(csvFilePath_overview)
                .then((jsonObj)=>{
                    try {
                        let pathSmellAll = path.join(__dirname,'overview','smell-all.json');
                        fs.writeFileSync(pathSmellAll, JSON.stringify(jsonObj,null,2));
                        
                    } catch (err) {
                        console.error(err);
                    }
                });
                let pathProcessData = path.join(__dirname,'preProcessing','processData.py');
                let process_getDataArray = require('child_process').spawn('python3', [pathProcessData,projName.toLowerCase()]);
                process_getDataArray.on('close',(code)=>{
                    console.log(`detailedClass exited with ${code}`);
                    ipc.send('get-smell-finished',"get-smell-done");
                });
            }
            else{
                alert("No smell detected from the given source!")
            }
    });    
};