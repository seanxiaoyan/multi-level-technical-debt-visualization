const {app, BrowserWindow} = require('electron');

function createWindow () {
    
    window = new BrowserWindow({
        webPreferences: {
            nodeIntegration: true,
            enableRemoteModule: true
            
        },
        width: 2400, height: 1800
    });
    window.loadFile('./index.html');
    const ipc = require('electron').ipcMain;
    // listen on ipc channel wait for GetSmells completed
    ipc.on('get-smell-finished', function(event,arg){
        window.loadFile('./overview/overview.html');
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
