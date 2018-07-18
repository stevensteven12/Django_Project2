import logging

from channels import Group
from channels.handler import AsgiHandler
from django.http import HttpResponse
import random
import threading
import multiprocessing
import time
import datetime as datetime
import json
from echo_example.models import tbIndexTable


logger = logging.getLogger(__name__)


"""""
#def ws_connect(message):
#    message.reply_channel.send({'accept': True})


def ws_receive(message): # ASGI WebSocket packet-received and send-packet message types # both have a "text" key for their textual data.
  message.reply_channel.send({ "text": message.content['text'], })


def ws_add(message): # Accept the connection
    message.reply_channel.send({"accept": True})
    # Add to the chat group
    Group("chat").add(message.reply_channel)


# Connected to websocket.receive
#def ws_message(message):
#    Group("chat").send({ "text": "[user] %s" % message.content['text'], })


# Connected to websocket.disconnect
def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)
"""""


def sendmsg(num):
    Group('chat').send({'text': num})


t = 0


def periodic():
    global t;
    n = random.randint(100, 200);
    sendmsg(str(n))
    t = threading.Timer(1, periodic)
    t.start()


def ws_message(message):
    global t
    print(message.content['text'])
    if (message.content['text'] == "start"):
        periodic()
    elif (message.content['text'] == "stop"):
        t.cancel()
    elif (message.content['text'] == "draw"):
        t.cancel()

    elif ("rawdata" in message.content['text']):
        ClientLastRow= message.content['text'].replace("rawdata_", "")
        periodic_rawdata(int(ClientLastRow))
    elif (message.content['text'] == "candlestick"):

        periodic_candlestick()
        """""
        f = open('echo_example/templates/IndexTable_TX00.Txt', 'r')
#        content = f.read()

        lines = f.read().split("\n")
        line_length= len(lines)
        if line_length > 1:
            line_length = len(lines) - 1  # the last row is empty
        f.close();

        SaveList = [] # for import a txt file into db
        response_data = [[0 for i in range(5)] for j in range(line_length)]
        for index in range(line_length):
                word = lines[index].split(",")
                if (len(word) > 5):
                    response_data[index][0]= word[3]
                    response_data[index][1] = int(word[5])
                    response_data[index][2] = int(word[4])
                    response_data[index][3] = int(word[6])
                    response_data[index][4] = int(word[7])

                    blog = tbIndexTable(StockNO= word[1], TickTime= word[3], P_Open= word[4], P_High= word[5], P_Low= word[6], P_Close= word[7],
                                        TradeQty= word[8], Ave_Price= word[9], Red= word[10])
                    SaveList.append(blog)

        tbIndexTable.objects.bulk_create(SaveList)
#        Group('chat').send({'text': str(line_length)})        
        Group('chat').send({'text': json.dumps(response_data)})
        """""

    else:
        Group('chat').send({'text': message.content['text']})
        # message.reply_channel.send({'text':'200'})


def ws_connect(message):
    message.reply_channel.send({"accept": True})
    Group('chat').add(message.reply_channel)
    Group('chat').send({'text': 'connected'})


def ws_disconnect(message):
    Group('chat').send({'text': 'disconnected'})
    Group('chat').discard(message.reply_channel)


def periodic_candlestick():
    global t;
    f = open('echo_example/templates/IndexTable_TX00.Txt', 'r')
    lines = f.read().split("\n")
    line_length = len(lines)
    if line_length > 1:
        line_length = len(lines) - 1  # the last row is empty
    f.close();

    response_data = [[0 for i in range(5)] for j in range(line_length)]
    for index in range(line_length):
        word = lines[index].split(",")
        if (len(word) > 5):
            response_data[index][0] = word[2] + " " + word[3]
            response_data[index][1] = int(word[5])
            response_data[index][2] = int(word[4])
            response_data[index][3] = int(word[6])
            response_data[index][4] = int(word[7])
    sendmsg(json.dumps(response_data))

    t = threading.Timer(5, periodic_candlestick)
    t.start()


def periodic_rawdata(ClientLastRow):
    global t;

    f_step = open('echo_example/templates/StepData_TX00.Txt', 'r')
    lines = f_step.read().split("\n")
    line_length = len(lines)
    if line_length > 0:
        line_length = len(lines) - 1  # the last row is empty
    f_step.close()

    word = lines[line_length - 1].split(",")
    ServerLastRow= int(word[13])
    StratRow= line_length - (ServerLastRow - ClientLastRow)

    if line_length - StratRow > 500:
        StratRow = line_length - 100

    response_data = "MMM" # change next line
    for index in range(StratRow, line_length):
        response_data = response_data + lines[index] + "MMM"

    if StratRow <= line_length - 1:
        sendmsg(response_data)

#    sendmsg('TX00, StratRow: ' + str(StratRow) +',  line_length:' + str(line_length) + ', ServerLastRow:' + str(ServerLastRow) + "MMM")

    t = threading.Timer(3, periodic_rawdata, [ServerLastRow])
    t.start()


    """""    
def periodic_rawdata(ClientLastRow):
    global t;

    f_step = open('echo_example/templates/StepData_TX00.Txt', 'r')
    lines = f_step.read().split("\n")
    line_length = len(lines)
    if line_length > 0:
        line_length = len(lines) - 1  # the last row is empty
    f_step.close()

    word = lines[line_length - 1].split(",")
    ServerLastRow= int(word[13])
    StratRow= line_length - (ServerLastRow - ClientLastRow)
    response_data = "MMM" # change next line
    for index in range(StratRow, line_length):
        response_data = response_data + lines[index] + "MMM"

    if StratRow <= line_length - 1:
        sendmsg(response_data)

    t = threading.Timer(3, periodic_rawdata, [ServerLastRow])
    t.start()
    """""

