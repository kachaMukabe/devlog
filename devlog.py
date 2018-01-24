import sys
import os

import datetime


def devlog():
    arg = sys.argv[1] if sys.argv.__len__() > 1 else None
    if arg is None:
        log()
    elif '-l' == arg:
        save_log(sys.argv[2])
    elif '-h' == arg or '--help' == arg:
        print_help()
    else:
        print("Type devlog -h or devlog --help to see all commands")


def log():
    log_m = input('Log: ')
    save_log(log_m)


def save_log(m):
    path = os.path.join(os.path.expanduser('~'), 'Documents')
    date = datetime.datetime.now()
    day = date.strftime("%d-%m-%Y")
    time = date.strftime("%H:%M")
    file = open(os.path.join(path, 'Devlog/devlog.md'), "w")
    file.write('{} {} {}'.format(day, time, m))
    file.close()
    print(m)


def list_logs():
    pass


def print_help():
    print('Help')


def check_dir(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)


devlog()
