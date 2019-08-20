import asyncio
import json
from datetime import datetime

import websockets

# TODO: maybe use db
msgs = []
clients = set()


class Client:
    def __init__(self, name, socket):
        self.name = name
        self.socket = socket


class Message:
    def __init__(self, author, text):
        self.time = datetime.now()
        self.text = text.replace("\n", "<br>")
        self.author = author

    def to_html(self):
        html = """
        <div class=msg>
        <h3>From {}:</h3>
        <p>{}</p>
        <p>At:{}</p>
        </div>
        """.format(self.author, self.text, self.time)
        return html


def get_author_by_socket(socket):
    for elem in clients:
        if elem.socket == socket:
            return elem.name
    return None


async def echo(websocket, path):
    async for message in websocket:
        if get_author_by_socket(websocket) is None:
            name = message
            clients.add(Client(name, websocket))
        else:
            msgs.append(Message(get_author_by_socket(websocket), message))
        await note_all()


async def trysend(client, msg):
    try:
        await client.socket.send(msg)
    except:
        clients.remove(client)


async def note_all():
    print(json.dumps([i.to_html() for i in msgs]))
    for i in list(clients):
        await trysend(i, json.dumps([i.to_html() for i in msgs]))


if __name__=="__main__":
    start_server = websockets.serve(echo, "localhost", 8081)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
