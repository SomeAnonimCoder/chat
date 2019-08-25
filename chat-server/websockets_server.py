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
    def __init__(self, author, text, html_class=""):
        self.time = datetime.now()
        self.html_class = html_class
        self.text = text.replace("\n", "<br>")
        self.author = author

    def to_html(self):
        if self.html_class:
            html = """
            <div class="msg {}">
            <h3>From {}:</h3>
            <p>{}</p>
            <p>At:{}</p>
            </div>
            """.format(self.html_class, self.author, self.text, self.time)
        else:
            html = """
                       <div class="msg">
                       <h3>From {}:</h3>
                       <p>{}</p>
                       <p>At:{}</p>
                       </div>
                       """.format(self.author, self.text, self.time)
        return html


def get_author_by_socket(socket):
    for elem in clients:
        if elem.socket == socket:
            return elem
    return None


def get_author_by_name(name):
    for elem in clients:
        if elem.name == name:
            return elem
    return None

def get_names_list():
    ret = "<ul>\n"
    for elem in clients:
        ret+="<li>{}</li>\n".format(elem.name)
    ret+="</ul>"
    return ret


async def process_message(websocket, path):
    async for message in websocket:
        if get_author_by_socket(websocket) is None:
            name = message
            if get_author_by_name(name) is None:
                clients.add(Client(name, websocket))
                msgs.append(Message("SysOp", "{} connected. Hello, {}!".format(name, name),"sysop"))
            else:
                await(websocket.send("ERR:EXISTING_NAME"))
        else:
            msgs.append(Message(get_author_by_socket(websocket).name, message))
        await note_all()


async def trysend(client, msg):
    try:
        await client.socket.send(msg)
    except:
        clients.remove(client)
        msgs.append(Message("SysOp", "You won't believe, gentlemen, we have a terrible loose again. <b>{}</b> left us.".format(client.name), "sysop"))
        await note_all()


async def note_all():
    for i in list(clients):
        await trysend(i, json.dumps([get_names_list()] +[i.to_html() for i in msgs]))


if __name__ == "__main__":
    start_server = websockets.serve(process_message, "localhost", 8081)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
