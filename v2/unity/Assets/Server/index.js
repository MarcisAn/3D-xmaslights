const io = require("socket.io-client");
const fs = require("fs");

const socketio = io.connect("ws://raspberrypi:3000");

socketio.on("connect", function (socket) {
  sendData();
  //while (true) {
  //  try {
  //    const data = fs.readFileSync("../lightdata.txt", "utf8");
  //    console.log(data);
  //    socketio.emit("lightdata", "a");
  //    socketio.send("cavata");
  //  } catch (err) {
  //    console.error(err);
  //  }
  //}
  console.log("connected");
  socketio.on("hello", (args) => {
    console.log(args);
  });
});
function sendData() {
  setTimeout(function () {
    const data = fs.readFileSync("../lightdata.txt", "utf8");
    socketio.emit("lightdata", data);
    sendData();
  }, 20);
}
