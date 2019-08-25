sr/bin/python3 -m virtulenv venv
source venv/bin/activate
pip install websockets websockets-client
python3 chat-server/server.py &
python3 chat-server/websockets_server.py &
