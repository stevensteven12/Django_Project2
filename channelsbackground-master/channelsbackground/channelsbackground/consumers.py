from django.shortcuts import render

def hello(message):
    print("Hello, Channels! " + message['name'])  # long running task or printing


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