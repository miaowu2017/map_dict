#-*-coding:utf-8-*-
from socket import *
from threading import Thread
from time import ctime
import os,sys
reload(sys)
sys.setdefaultencoding('utf-8')
HOST = "127.0.0.1"
PORT = 9999
CONN_MAXN = 100
BUF_SZ = 1024
ADDR = (HOST,PORT)
LAST_LINE = 15
servSocket = socket(AF_INET,SOCK_STREAM)
servSocket.bind(ADDR)
servSocket.listen(CONN_MAXN)
print "server working..."
def handleClnt(clntSocket):
    try:
        data = clntSocket.recv(BUF_SZ)
    except:
        clntSocket.close()
        return
    with open('long.log','a') as log:
        log.write('[%s]' % ctime())
        log.write('\t')
        log.write(data)
        log.write('\n')
        log.close()
    with open('clnt.log','a') as log:
        log.write('[%s]' % ctime())
        log.write('\t')
        log.write(data)
        log.write('\n')
        log.close()
    with open('clnt.log','r') as log:
        lines = log.readlines()
        if len(lines)>LAST_LINE:
            lines = lines[-LAST_LINE:]
        log.close()
    with open('clnt.log','w') as log:
        log.writelines(lines)
        log.close
    clntSocket.close()

while True:
    clntSocket, addr = servSocket.accept()
    print "[%s]"%(ctime(),),addr," on line."
    clntSocket.send(os.popen('type clnt.log').read())
    t = Thread(target=handleClnt,args=(clntSocket,))
    t.start()
    t.join(timeout=1)



