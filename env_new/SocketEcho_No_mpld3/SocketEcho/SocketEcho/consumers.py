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
#  from echo_example.models import tbIndexTable
import os
import pdb


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
    #    t.cancel()
        periodic_candlestick()
    elif (message.content['text'] == "candlestick_svg"):

        periodic_candlestick_svg()

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
    f = open('echo_example/static/IndexTable_TX00.Txt', 'r')
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


def periodic_candlestick_svg():
    global t;

    if os.path.isfile('echo_example/static/IndexTable_TX00.Txt'):
        f = open('echo_example/static/IndexTable_TX00.Txt', 'r')
        lines = f.read().split("\n")
        line_length = len(lines)
        if line_length > 1:
            line_length = len(lines) - 1  # the last row is empty
        f.close();

        response_data = [[0 for i in range(6)] for j in range(line_length)]
        for index in range(line_length):
            word = lines[index].split(",")
            if (len(word) > 6):
            #    response_data[index][0] = word[2] + " " + word[3]
                response_data[index][0] = word[3]
                response_data[index][1] = int(word[4])
                response_data[index][2] = int(word[5])
                response_data[index][3] = int(word[6])
                response_data[index][4] = int(word[7])
                response_data[index][5] = int(word[8])
        sendmsg(json.dumps(response_data))

    t = threading.Timer(60, periodic_candlestick_svg)
    t.start()


def periodic_rawdata(ClientLastRow): # client to server
    global t;

    parse_updatedata()

    ServerLastRow= 0
    if os.path.isfile('echo_example/static/StepData_TX00.Txt'):
        f_step = open('echo_example/static/StepData_TX00.Txt', 'r')
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

    t = threading.Timer(3, periodic_rawdata, [ServerLastRow])
    t.start()


def parse_updatedata(): # server parse temp updat_data and delete it
    IsSummaryExist= False
    SummaryCycle= 0
    if os.path.isfile('echo_example/static/Summary_TX00.Txt'):
        IsSummaryExist= True
        f_summary = open('echo_example/static/Summary_TX00.Txt', 'r')
        lines_summary = f_summary.read().split("\n")
        lines_summary_len = len(lines_summary)
        if lines_summary_len >= 3:
            SummaryCycle= int(lines_summary[2])
        f_summary.close()

#    pdb.set_trace()
    ServerLast_update= 0
    if IsSummaryExist & os.path.isfile('echo_example/static/UpdateData_TX00.Txt'):
        print("UpdateData_TX00 exit--1")
        f_update = open('echo_example/static/UpdateData_TX00.Txt', 'r')
        lines_update = f_update.read().split("\n")
        line_length_update = len(lines_update)
        if line_length_update > 1:
            line_length_update = len(lines_update) - 1  # the last row is empty
        word_update = lines_update[line_length_update - 1].split(",")
        if len(word_update) >= 13:
            ServerLast_update = int(word_update[13])
            print("UpdateData date-- 2:" + str(ServerLast_update))

            add_line = '';
            if SummaryCycle <= ServerLast_update:
                if os.path.isfile('echo_example/static/StepData_TX00.Txt'):
                    print("StepData_TX00 exist--3")
                    f_step = open('echo_example/static/StepData_TX00.Txt', 'r')
                    lines_step = f_step.read().split("\n")
                    line_length_step = len(lines_step)
                    print("StepData_TX00 exist--3-1" + str(line_length_step))
                    if line_length_step > 1:
                        line_length_step = len(lines_step) - 1  # the last row is empty
                    word_step = lines_step[line_length_step - 1].split(",")
                    if len(word_step) >= 13:
                        ServerLast_step = int(word_step[13])

                        print("StepData date--4: " + str(ServerLast_step))
                        f_step.close()
                        if SummaryCycle <= ServerLast_step:
                            temp_str= '';
                            for index in range(line_length_update):
                                temp_str = temp_str + lines_update[index] + '\n'
                            f_step = open('echo_example/static/StepData_TX00.Txt', 'a')
                            f_step.write(temp_str)
                            f_step.close();

                            print("UpdateData deleted OK--5")
                            os.remove("echo_example/static/UpdateData_TX00.Txt")
                        else:
                            os.remove("echo_example/static/StepData_TX00.Txt")
                            print("StepData deleted NG--6")
                    else:
                        print("StepData copy from UpdateData--7")
                        add_line = ""
                        f_step = open('echo_example/static/StepData_TX00.Txt', 'w')
                        for index in range(line_length_update):
                            add_line = add_line + lines_update[index] + '\n'
                        f_step.write(add_line)
                        f_step.close()
                else:
                    print("StepData copy from UpdateData--7-1")
                    add_line= ""
                    f_step = open('echo_example/static/StepData_TX00.Txt', 'w')
                    for index in range(line_length_update):
                        add_line= add_line + lines_update[index] + '\n'
                    f_step.write(add_line)
                    f_step.close()
            else:
                print("UpdateData_TX00 deleted NG--8")
                if os.path.isfile('echo_example/static/StepData_TX00.Txt'):
                    os.remove("echo_example/static/StepData_TX00.Txt")
                f_step = open('echo_example/static/StepData_TX00.Txt', 'w')
                for index in range(line_length_update):
                    add_line = add_line + lines_update[index] + '\n'
                    f_step.write(add_line)
                f_step.close()

        f_update.close();

    if IsSummaryExist:
        f_summary = open('echo_example/static/Summary_TX00.Txt', 'r')
        lines_summary = f_summary.read().split("\n")
        lines_summary_len = len(lines_summary)

        temp_str = ''
        step_last= 0;
        if os.path.isfile('echo_example/static/StepData_TX00.Txt'):
            f_step = open('echo_example/static/StepData_TX00.Txt', 'r')
            lines_step = f_step.read().split("\n")
            line_length_step = len(lines_step)
            if line_length_step > 1:
                line_length_step = len(lines_step) - 1  # the last row is empty
            word_step = lines_step[line_length_step - 1].split(",")
            step_last=  int(word_step[13])

        if SummaryCycle <= step_last:
            if ServerLast_update == 0:
                ServerLast_update = step_last

            for index in range(lines_summary_len - 1):
                if index != 2:
                    temp_str = temp_str + lines_summary[index] + '\n'
                else :
                    temp_str= temp_str + str(ServerLast_update) + '\n'

            print("StepData Date--10:" + str(step_last))
            f_summary.close()
            f_summary = open('echo_example/static/Summary_TX00.Txt', 'w')
            f_summary.write(temp_str)
        elif os.path.isfile('echo_example/static/StepData_TX00.Txt'):
            os.remove("echo_example/static/StepData_TX00.Txt")
            print("no StepData Date--11:" + str(step_last))

        f_summary.close()

#if __name__ == '__main__':
#    parse_updatedata()