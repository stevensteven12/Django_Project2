from channels.routing import route

from .consumers import  hello, websocket_receive

channel_routing = [
    route('background-hello', hello),
    route("websocket.receive", websocket_receive, path=r"^/chat/"),
]
