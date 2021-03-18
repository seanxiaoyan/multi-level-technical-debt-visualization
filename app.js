const {app, BrowserWindow} = require('electron');
const path = require('path');

function createWindow () {
    
    window = new BrowserWindow({
        webPreferences: {
            nodeIntegration: true,
            enableRemoteModule: true
            
        },
        width: 2400, height: 1800
    });
    let pathIndex = path.join(__dirname,'index.html');
    window.loadFile(pathIndex);
    const ipc = require('electron').ipcMain;
    // listen on ipc channel wait for GetSmells completed
    let pathOverview = path.join(__dirname,'overview','overview.html');
    ipc.on('get-smell-finished', function(event,arg){
        window.loadFile(pathOverview);
    });


};

app.on('ready', createWindow);

app.on('window-all-closed', () => {
    // On macOS it is common for applications and their menu bar
    // to stay active until the user quits explicitly with Cmd + Q
    if (process.platform !== 'darwin') {
      app.quit()
    };
});
