const fs = require('fs');
const express = require('express');
var app = express();
let httpsOptions = {
  key: fs.readFileSync('./key.pem'),
  cert: fs.readFileSync('./cert.pem')
};

var io;

if (process.env.MODE === 'https') {
  var https = require('https').createServer(httpsOptions, app);
  io = require('socket.io')(https);
  https.listen(3443, function() {
    console.log('listening on https:*3443');
  });
} else {
  var http = require('http').Server(app);
  io = require('socket.io')(http);
  http.listen(3080, function() {
    console.log('listening on *:3080');
  });
}

app.get('/*', (req, res) => {
  res.sendFile(__dirname + '/public/index.html');
});

let latest = {};

let phones = new Map();
let clients = new Map();

io.of('/phones').on('connection', function(socket) {
  let id;
  socket.emit('identify', i => {
    console.log('connected phone with id: ', i);
    id = i.toString();
    let arr = phones.get(id) || [];
    arr.push(socket);
    phones.set(id, arr);
  });
  socket.on('disconnect', () => {
    let arr = phones.get(id) || [];
    let i = arr.indexOf(socket);
    if (i > -1) arr.splice(i, 1);
    phones.set(arr, id);
    console.log('disconnected phone with id: ', id);
  });
  socket.on('geolocation', position => {
    if (id) {
      (clients.get(id) || []).forEach(c => c.emit('geolocation', position));
    }
  });
  socket.on('orientation', orientation => {
    if (id) {
      (clients.get(id) || []).forEach(c => c.emit('orientation', orientation));
    }
  });
});

io.of('/clients').on('connection', function(socket) {
  let id;
  socket.emit('identify', i => {
    console.log('connected client with id: ', i);
    id = i.toString();
    let arr = clients.get(id) || [];
    arr.push(socket);
    clients.set(id, arr);
  });
  socket.on('disconnect', () => {
    let arr = clients.get(id) || [];
    let i = arr.indexOf(socket);
    if (i > -1) arr.splice(i, 1);
    clients.set(arr, id);
    console.log('disconnected client with id: ', id);
  });
  socket.on("get_picture", fn => {
    console.log("get_picture");
    let phone = (phones.get(id) || [])[0];
    if(!phone) {
      return fn(null);
    }
    phone.emit("get_picture", pic => {
      fn(pic);
    });
  });
});
