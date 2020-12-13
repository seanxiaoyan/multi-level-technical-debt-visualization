const { electron } = require('process');

const ipc = require('electron').ipcRenderer;

function detectSmell(){

    //set config.ini for GetSmells
    var proj_path = '/Users/seanxu/Desktop/calcite';
    var subprocess1 = require('child_process').spawn('python3', ['./preProcessing/setconfig.py',proj_path]);


    subprocess1.on('close',(code)=>{
        console.log(`set config exited with ${code}`);

    });


    //set PYTHONPATH for GetSmells and Execute GetSmells
    console.log('Current directory: ' + process.cwd());
    var subprocess2 = require('child_process').exec('./preProcessing/getsmell.sh');
    subprocess2.stdout.on('data',function(data){
        document.getElementById("progressBar").innerHTML = data.toString('utf8');
        // ipc.send('get-smell-proceeding',data.toString('utf8'))
        });
          
    
    subprocess2.on('close',(code)=>{
            console.log(`set PYTHONPATH and execute GetSmells process exited with code ${code}`);
            ipc.send('get-smell-finished',"get-smell-done")

        });

        
};