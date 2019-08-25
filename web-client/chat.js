let name = window.prompt("Pick a username:")
let socket = new WebSocket("ws://localhost:8081");
let username = document.getElementById("username");
username.innerHTML = ("Howdy, "+name + "!");
let msg = document.getElementById("message");
let msgs = document.getElementById("messages");
let sendBtn = document.getElementById("send");
sendBtn.onclick = function(){
    socket.send(msg.value);
    msg.value="";
}

socket.onopen=function(){
socket.send(name)
}
socket.onmessage = function(event) {
    if (event.data=="ERR:EXISTING_NAME"){
    window.confirm("This name already exists in chat!Take another?")
    }
    json = JSON.parse(event.data)
    html = ""
    for(i=0;i<json.length;i++){
        html+=json[i];
        }
    msgs.innerHTML = html;
};

socket.onclose = function(event) {
    if(confirm("Connection interrupted. Reconnect?")){
        socket = new WebSocket("ws://localhost:8081");
    }
};

socket.onerror = function(error) {
  alert(`[error] ${error.message}`);
};
