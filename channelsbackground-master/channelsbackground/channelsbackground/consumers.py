import requests
import time


def hello(message):
    print("Hello, Channels! " + message['name'])  # long running task or printing

#    time.sleep(3)
#    r = requests.get('http://127.0.0.1:8000/')
#    print("content-type:" + r.headers['content-type'] + ", " + message['name'])


def websocket_receive(message):
    text = message.content.get('text')
    if text:
        message.reply_channel.send({"text": "Everyone said: {}".format(text)})


"""
def websocket_receive(message):
    text = message.content.get('text')
    if text:
        message.reply_channel.send({"text": "You said: {}".format(text)})

    return render(request, template, locals(), )
"""