
const SERVER = "127.0.0.1"
const socket = io();

var receivedMsgLog = []



socket.on('connect', () => {
    console.log('connected');
})

socket.on('disconnect', () => {
    console.log('disconnect');
})

socket.on('message', (msg) => {
    console.log(msg);
    receivedMsgLog.append(msg);
})


function sendMsg(msg){
    socket.emit('message', msg);  
}


function msgPacker(x,y,z){
    
    return (x,y,z)
}




