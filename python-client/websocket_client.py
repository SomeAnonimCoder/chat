from websocket import WebSocketApp

ws = WebSocketApp("ws://localhost/:8081",
                          on_message = print,
                          on_close=print("close"),
                          on_error = print)
ws.run_forever()
ws.send("asdfgfds")
ws.send("AFESzrgdthfnxbf")
ws.send("AFESzrgdthfnxbf")
ws.send("AFESzrgdthfnxbf")