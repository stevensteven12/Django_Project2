from channels.routing import route
from realtime.consumers import websocket_receive

channel_routing = [
    route("websocket.receive", websocket_receive, path=r"^/chat/"),
]