const electron = require('electron');
const {app,BrowserWindow,Notification} = electron;


// 新しいウィンドウ(Webページ)を生成
let win;
function createWindow() {
  // BrowserWindowインスタンスを生成
  win = new BrowserWindow({width: 800, height: 600});
  // index.htmlを表示
  win.loadURL('http://0.0.0.0:80/');
  // デバッグするためのDevToolsを表示
  //win.webContents.openDevTools();
  // ウィンドウを閉じたら参照を破棄
  win.on('closed', () => {   // ()は　function ()と書いていい
    win = null;
  });
}
// アプリの準備が整ったらウィンドウを表示
app.on('ready', () =>{
  
  if(Notification.isSupported()){
  const notification = new Notification({
    title:'TegeTege Darts Sys.',
    body:'目指せハットトリック!' 
  })
  notification.on('show',() => console.log('Notification shown'))
  notification.show()
  createWindow();
  }else{
    console.log('デスクトップ通知に非対応です')
  }
  });

// 全てのウィンドウを閉じたらアプリを終了
app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});
app.on('activate', () => {
  if (win === null) {
    createWindow();
  }
});









// const mainWindow = null;
// app.on('window-all-closed', function () {
//     //if (process.platform != 'darwin')
//         app.quit();
// });
// app.on('ready', function () {
//     // ブラウザ(Chromium)の起動, 初期画面のロード
//     win = new BrowserWindow({width: 1000, height: 600});
//     mainWindow.loadUrl('file://' + __dirname + '/index.html');
//     mainWindow.on('closed', function () {
//         mainWindow = null;
//     });
// });

//参照サイト
//https://qiita.com/mamosan/items/084039c3e6d703b7b45f