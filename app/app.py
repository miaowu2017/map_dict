#-*-coding:utf-8-*-
# TODO:开发通用的定长、变长、XML报文处理应用 - app类
from os import system
from mdlLog.testLog import testLog
import os
os.chdir('../mdlConfig/')
system('python initConfig.py')
from mdlCmncatin.serv import serv
from mdlDtExcge.variableLethHelper import variableLethHelper


class app(object):
    pass
def senddata(clntsocket):
    os.chdir('../app/')
    data = clntsocket.recv(1024)
    if data:
        print data
    try:
        data_send = variableLethHelper().unpack(data)
        try:
            clntsocket.send("|".join(data_send))
        except Exception as e:
            print e.message
            testLog.write('app.log', e.message)
            clntsocket.send("error")
    except Exception as e:
        print e.message
        testLog.write('app.log',e.message)
        clntsocket.send("error")

    clntsocket.close()
myserv = serv(host='127.0.0.1',port=1000,max_conn=100,clntsockfunc=senddata)
myserv.run()


