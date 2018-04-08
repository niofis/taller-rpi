const express = require("express");
var app = express();
var http = require("http").Server(app);
var io = require("socket.io")(http);

app.use(express.static(__dirname + "/interface/build"));
app.get("/*", (req, res) => {
  res.sendFile(__dirname + "/interface/build/index.html");
});

app.get("/geolocation", (req, res) => {
  res.json(latest.geolocation);
});

app.get("/orientation", (req, res) => {
  res.json(latest.orientation);
});

let latest = {};

let phones = new Map();
let clients = new Map();

io.of("/phones").on("connection", function(socket) {
  let id;
  socket.emit("identify", i => {
    console.log("connected phone with id: ", i);
    id = i.toString();
    let arr = phones.get(id) || [];
    arr.push(socket);
    phones.set(id, arr);
  });
  socket.on("disconnect", () => {
    let arr = phones.get(id) || [];
    let i = arr.indexOf(socket);
    if (i > -1)
      arr.splice(i, 1);
    phones.set(arr, id);
  });
  socket.on("geolocation", position => {
    if(id) {
      (clients.get(id) || []).forEach(c => c.emit("geolocation", position));
    }
  });
  socket.on("orientation", orientation => {
    if(id) {
      (clients.get(id) || []).forEach(c => c.emit("orientation", orientation));
    }
  });
});

io.of("/clients").on("connection", function(socket) {
  let id;
  socket.emit("identify", i => {
    console.log("connected client with id: ", i);
    id = i.toString();
    let arr = clients.get(id) || [];
    arr.push(socket);
    clients.set(id, arr);
  });
  socket.on("disconnect", () => {
    let arr = clients.get(id) || [];
    let i = arr.indexOf(socket);
    if (i > -1)
      arr.splice(i, 1);
    clients.set(arr, id);
  });
});

http.listen(3080, function() {
  console.log("listening on *:3080");
});
