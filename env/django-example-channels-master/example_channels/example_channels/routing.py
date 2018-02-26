from channels.routing import route
from example.consumers import ws_connect, ws_disconnect, websocket_receive


channel_routing = [
    route('websocket.connect', ws_connect),
    route('websocket.disconnect', ws_disconnect),
    route("websocket.receive", websocket_receive, path=r"^/chat/"),
]
