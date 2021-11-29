const { app, BrowserWindow, Menu } = require("electron")
require('electron-reload')(__dirname)


function createWindow() {
    const mainWindow = new BrowserWindow({
        // width: 1500,
        // height: 1000
        icon:'./UI/assets/about/MicrosoftTeams-image3.ico'
    })

    mainWindow.maximize();

    mainWindow.loadFile(__dirname + '/UI/loading.html')
    //mainWindow.webContents.openDevTools()
    mainWindow.setAutoHideMenuBar(true)

    // let menu = Menu.buildFromTemplate([{
    //         label: "File",
    //         submenu: [
    //             { label: 'Get Article' },
    //             {
    //                 label: 'Exit',
    //                 click() {
    //                     app.quit()
    //                 }
    //             }
    //         ]
    //     },
    //     { label: "About" }
    //
    // ])
    //
    // Menu.setApplicationMenu(menu)
}


app.whenReady().then(() => {
    createWindow()
})