const express = require('express');
const socketio = require("socket.io")
const Server = socketio.Server;
const app = express();
const server = app.listen(3000);
const io = new Server(server, { cors: { origin: '*' } });

fs = require("fs");
fs.writeFile("./lightdata.json", "ata",function (err) {
  if (err) return console.log(err);
  console.log('Hello World > helloworld.txt');
})

app.get("/" ,function(req,res){
res.send("helo world")
})

console.log("b");
io.on("connection", (socket) => {
 console.log("connected")
 	socket.emit("hello", "world");
	socket.on("lightdata", (data) => {
		//console.log(data)
		fs.writeFile("./lightdata.json",data,function(err){ if (err) return console.log(err);
		})
	})
});


io.onmessage = (data) =>{
	console.log(data);
};
