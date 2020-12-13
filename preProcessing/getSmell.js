const { electron } = require('process');

const ipc = require('electron').ipcRenderer;
const fs = require('fs');
const {dialog} = require('electron').remote;
const csv=require('csvtojson');

function detectSmell(){
    //set config.ini for GetSmells

    // use folder selector to get project path
    let pathArray = dialog.showOpenDialogSync({
        properties: ['openDirectory']
    });
    let proj_path = pathArray[0];
    console.log(proj_path);


    let subprocess1 = require('child_process').spawn('python3', ['./preProcessing/setconfig.py',proj_path]);


    subprocess1.on('close',(code)=>{
        console.log(`set config exited with ${code}`);

    });


    //set PYTHONPATH for GetSmells and Execute GetSmells
    console.log('Current directory: ' + process.cwd());
    let subprocess2 = require('child_process').exec('./preProcessing/getsmell.sh');
    subprocess2.stdout.on('data',function(data){
        document.getElementById("progressBar").innerHTML = data.toString('utf8');
        // ipc.send('get-smell-proceeding',data.toString('utf8'))
        });
          
    
    subprocess2.on('close',(code)=>{
            console.log(`set PYTHONPATH and execute GetSmells process exited with code ${code}`);
            // process csv for overview
            let splits = proj_path.split('/');
            let len = splits.length;
            let projName = splits[len-1];
            const csvFilePath = './GetSmells/getsmells-output/smells/'+projName+'.csv';
            if (fs.existsSync(csvFilePath)){
                csv()
                .fromFile(csvFilePath)
                .then((jsonObj)=>{
                    try {
                        fs.writeFileSync('./overview/smell-all.json', JSON.stringify(jsonObj,null,2));
                        ipc.send('get-smell-finished',"get-smell-done");
                    } catch (err) {
                        console.error(err);
                    }
                });
            }
            else{
                alert("No smell detected from the given source!")
            }
        });
    

    // // process csv for overview
    // let splits = proj_path.split('/');
    // let len = splits.length;
    // let projName = splits[len-1];
    // const csvFilePath = './GetSmells/getsmells-output/smells/'+projName+'.csv';
    // csv()
    // .fromFile(csvFilePath)
    // .then((jsonObj)=>{
    //     try {
    //         fs.writeFileSync('./overview/smell-all.json', JSON.stringify(jsonObj,null,2));
    //         ipc.send('get-smell-finished',"get-smell-done");
    //     } catch (err) {
    //         console.error(err);
    //     }
    // });
        
};