const { electron } = require('process');
const ipc = require('electron').ipcRenderer;
const fs = require('fs');
const {dialog} = require('electron').remote;
const csv=require('csvtojson');

let overviewReady = 0;
let detailedClassReady = 0;

function detectSmell(){
    //set config.ini for GetSmells
    // use folder selector to get project path
    let pathArray = dialog.showOpenDialogSync({
        properties: ['openDirectory']
    });
    let proj_path = pathArray[0];

    let process_config = require('child_process').spawn('python3', ['./preProcessing/setconfig.py',proj_path]);

    process_config.on('close',(code)=>{
        console.log(`set config exited with ${code}`);
    });

    //set PYTHONPATH for GetSmells and Execute GetSmells
    let process_detectsmell = require('child_process').exec('./preProcessing/getsmell.sh');
    process_detectsmell.stdout.on('data',function(data){
        document.getElementById("progressBar").innerHTML = data.toString('utf8');
    });
          
    let projName;
    process_detectsmell.on('close',(code)=>{
            console.log(`set PYTHONPATH and execute GetSmells process exited with code ${code}`);
            
            let splits = proj_path.split('/');
            let len = splits.length;
            projName = splits[len-1];
            const csvFilePath_overview = './GetSmells/getsmells-output/smells/'+projName+'.csv';

            // if smell detected, then proceed to process csv files
            if (fs.existsSync(csvFilePath_overview)){
                csv()
                .fromFile(csvFilePath_overview)
                .then((jsonObj)=>{
                    try {
                        fs.writeFileSync('./overview/smell-all.json', JSON.stringify(jsonObj,null,2));
                        
                    } catch (err) {
                        console.error(err);
                    }
                });
                let process_getDataArray = require('child_process').spawn('python3', ['./preProcessing/processData.py',projName.toLowerCase()]);
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