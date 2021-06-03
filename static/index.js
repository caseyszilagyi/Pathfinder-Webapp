    var express = require('express');
    var app = express();
    var http = require('http').createServer(app);
    var io = require('socket.io')(http);
    var PORT = process.env.PORT || 3000;
    console.log("yo");

    http.listen(PORT,function(){
        console.log("Listening to port " + PORT);
    });
        