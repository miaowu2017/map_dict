#-*-coding:utf-8-*-
from socket import *
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')
class clt(object):
    def __init__(self,host,port):
        self.host = host
        self.port = port

    def run(self):
        while True:
            self.cltSocket = socket(AF_INET,SOCK_STREAM)
            self.cltSocket.connect((self.host,self.port))
            print '*'*70
            self.cltSocket.send(raw_input('>'))
            try:
                print self.cltSocket.recv(1024)
            except Exception as e:
                print e.message
clt(host='127.0.0.1',port=1000).run()