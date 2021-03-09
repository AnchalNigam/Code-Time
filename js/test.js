var net = require('net');
net.createServer(function(socket) {
    socket.on('data', function(data) {
        console.log(data + '');        
        socket.write('server response\n');
        socket.write(data + '\n');
        socket.end();
    });
    socket.on('end', function(data) {
        console.log('client connection closed');
        process.exit();
    });
}).listen(8080);

var net_conn = net.createConnection(8080);
net_conn.on('connect', function() {
    console.log('client connected to server');
});
net_conn.on('error', function(err) {
    console.log('error in connection:', err);
    process.exit();
});
net_conn.write('client request');
net_conn.pipe(process.stdout);