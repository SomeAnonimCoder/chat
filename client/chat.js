name = window.prompt("Pick a username:")

let socket = new WebSocket("ws://localhost:8081");
let msg = document.getElementById("message");
let msgs = document.getElementById("messages");
let sendBtn = document.getElementById("send");
sendBtn.onclick = function(){
    socket.send(msg.value);
}

socket.onopen=function(){
socket.send("")
}
socket.onmessage = function(event) {
    json = JSON.parse(event.data)
    html = ""
    for(i=0;i<json.length;i++){
        html += "<p class=msg>";
        html+=json[i];
        html+="<\p>";
        }
    msgs.innerHTML = html;
};

socket.onclose = function(event) {
  if (event.wasClean) {
    alert(`[close] Соединение закрыто чисто, код=${event.code} причина=${event.reason}`);
  } else {
    // например, сервер убил процесс или сеть недоступна
    // обычно в этом случае event.code 1006
    alert('[close] Соединение прервано');
  }
};

socket.onerror = function(error) {
  alert(`[error] ${error.message}`);
};


