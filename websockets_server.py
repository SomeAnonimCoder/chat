import asyncio
import json

import websockets

msgs = []

clients = set()

async def echo(websocket, path):
    clients.add(websocket)
    async for message in websocket:
        if message:msgs.append(message)
        await note_all()

async def trysend(socket, msg):
    try: await socket.send(msg)
    except: clients.remove(socket)

async def note_all():
    print(msgs, clients)
    for i in list(clients):
        await trysend(i,json.dumps(msgs))


start_server = websockets.serve(echo, "localhost", 8081)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
