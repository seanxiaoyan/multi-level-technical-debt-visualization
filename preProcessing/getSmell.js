const { electron } = require('process');

const ipc = require('electron').ipcRenderer;
const fs = require('fs');

function detectSmell(){
    // //set config.ini for GetSmells
    let proj_path = '/Users/seanxu/Desktop/calcite';
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
            const csv=require('csvtojson') //. Make sure you have this line in order to call functions from this modules
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
        });
    

    // // process csv for overview
    // let splits = proj_path.split('/');
    // let len = splits.length;
    // let projName = splits[len-1];
    // const csvFilePath = './GetSmells/getsmells-output/smells/'+projName+'.csv';
    // const csv=require('csvtojson') //. Make sure you have this line in order to call functions from this modules
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