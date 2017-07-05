#-*-coding:utf-8-*-
'''
serv.py --- a simple server
'''
from socket import *
import sys
from time import ctime
from threading import Thread
from mdlLog.testLog import testLog
reload(sys)
sys.setdefaultencoding('utf-8')
class serv(object):
    def __init__(self,host,port,max_conn,logfile):
        self.servSocket = socket(AF_INET, SOCK_STREAM)
        self.servSocket.bind((host,port))
        self.max_conn = max_conn
        self.func = self.foo
        self.logfile = logfile
    def foo(self,clntsocket,trxcode='99999'):
        #接收数据
        data = clntsocket.recv(1024)
        if data:
            print data
        #返回数据
        clntsocket.send('hello client')
        clntsocket.close()
    def importfunc(self,func):
        self.func = func
    def importtrxcode(self,trxcode):
        self.trxcode = trxcode
    def run(self):
        self.servSocket.listen(self.max_conn)
        print 'serv working...'
        while True:
            clntSocket, addr = self.servSocket.accept()
            print 'on line [%s]'%ctime(),addr
            testLog.write(self.logfile,'on line [%s]'%ctime()+str(addr))
            try:
                t = Thread(target=self.func,args=(clntSocket,self.trxcode))
                t.start()
                t.join(timeout=1)
            except Exception as e:
                testLog.write(self.logfile,e.message)
# serv(host='127.0.0.1',port=9999,max_conn=10,logfile='currentapp.log').run()