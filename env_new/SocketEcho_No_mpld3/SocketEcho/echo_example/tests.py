from django.test import TestCase
import os
import pdb

def parse_updatedata(): # server parse temp updat_data and delete it
    line_length_update= 0
    pdb.set_trace()
    if os.path.isfile('echo_example/static/UpdateData_TX00.Txt'):
        f_update = open('echo_example/static/UpdateData_TX00.Txt', 'r')
        lines_update = f_update.read().split("\n")
        line_length_update = len(lines_update)
        if line_length_update > 1:
            line_length_update = len(lines_update) - 1  # the last row is empty
        word_update = lines_update[line_length_update - 1].split(",")
        ServerLast_update = int(word_update[13])
        Update_Date= word_update[2]
        f_update.close();

        if os.path.isfile('echo_example/static/StepData_TX00.Txt'):
            f_step = open('echo_example/static/StepData_TX00.Txt', 'r')
            lines_step = f_step.read().split("\n")
            line_length_step = len(lines_step)
            if line_length_step > 1:
                line_length_step = len(lines_step) - 1  # the last row is empty
            word_step = lines_update[line_length_step - 1].split(",")
            ServerLast_step = int(word_step[13])
            Step_Date= word_step[2]
            f_step.close()
            if Update_Date > Step_Date:
                os.remove("echo_example/static/StepData_TX00.Txt")
            elif Update_Date == Step_Date:
                temp_str= '';
                for index in range(line_length_update):
                    temp_str = temp_str + lines_update[index] + '\n'
                f_step = open('echo_example/static/StepData_TX00.Txt', 'a')
                f_step.write(temp_str)
                f_step.close();

        os.remove("echo_example/static/UpdateData_TX00.Txt")

    if os.path.isfile('echo_example/static/Summary_TX00.Txt'):
        f_summary = open('echo_example/static/Summary_TX00.Txt', 'r')
        lines_summary = f_summary.read().split("\n")
        lines_summary_len = len(lines_summary)
        temp_str = ''
        for index in range(lines_summary_len - 1):
            if index != 2:
                temp_str = temp_str + lines_summary[index] + '\n'
            else :
                temp_str= temp_str + str(ServerLast_update) + '\n'

        f_summary.close()
        f_summary = open('echo_example/static/Summary_TX00.Txt', 'w')
        f_summary.write(temp_str)
        f_summary.close()


if __name__ == '__main__':
    parse_updatedata()