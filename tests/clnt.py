#-*-coding:utf-8-*-
from socket import *
from rndName import getRndName
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
HOST = "127.0.0.1"
PORT = 9999
CONN_MAXN = 100
BUF_SZ = 1024
ADDR = (HOST,PORT)
NAME = getRndName()
# NAME utf-8
LAST_LINE = 10
MAX_WAIT_TIME = 2
def readlog():
    content = clntSocket.recv(BUF_SZ)
    lines = content.split('\n')
    if len(lines) < LAST_LINE:
        for line in lines:
            print line.rstrip('\n')
    else:
        for line in lines[-LAST_LINE:]:
            print line.rstrip('\n')
def clear():
    import os
    os.system("cls")
while True:
    clntSocket = socket(AF_INET, SOCK_STREAM)
    clntSocket.connect(ADDR)
    clear()
    readlog()
    print '-'*70
    data = raw_input("[%s]>"%NAME).rstrip('\n')
    clntSocket.send("[%s]\t%s" % (NAME, data))