#-*-coding:utf-8-*-
'''
serv.py --- a simple server
'''
from socket import *
import sys
from time import ctime
from threading import Thread
reload(sys)
sys.setdefaultencoding('utf-8')
class serv(object):
    def __init__(self,host,port,max_conn,clntsockfunc):
        self.servSocket = socket(AF_INET, SOCK_STREAM)
        self.servSocket.bind((host,port))
        self.max_conn = max_conn
        self.clntsockfunc = clntsockfunc
    def run(self):
        self.servSocket.listen(self.max_conn)
        print 'serv working...'
        while True:
            clntSocket, addr = self.servSocket.accept()
            print 'on line [%s]'%ctime(),addr
            t = Thread(target=self.clntsockfunc,args=(clntSocket,))
            t.start()
            t.join(timeout=1)
def senddata(clntsocket):
    data = clntsocket.recv(1024)
    if data:
        print data
    clntsocket.send('hello client')
    clntsocket.close()
serv(host='127.0.0.1',port=9999,max_conn=10,clntsockfunc=senddata).run()