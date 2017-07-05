#-*-coding:utf-8-*-
# TODO:开发通用的定长、变长、XML报文处理应用 - app类
from os import system
from mdlLog.testLog import testLog
import os
os.chdir('../mdlConfig/')
system('python initConfig.py')
from mdlCmncatin.serv import serv
from mdlDtExcge.variableLethHelper import variableLethHelper
from mdlDtExcge.fixedLethHelper import fixedLethHelper
from mdlDtExcge.xmlHelper import xmlHelper
# 定长报文、变长报文的处理逻辑
def fixedfoo(clntsocket):
    # 接收数据
    data = clntsocket.recv(1024)
    if data:
        print data
    # 返回数据
    try:
        clntsocket.send(",".join(fixedLethHelper().unpack(data)))
    except:
        clntsocket.send('error')
    clntsocket.close()
def variablefoo(clntsocket):
    # 接收数据
    data = clntsocket.recv(1024)
    if data:
        print data
    # 返回数据
    try:
        clntsocket.send(variableLethHelper().unpack(data))
    except:
        clntsocket.send('error')
    clntsocket.close()
fixedServ = serv(host='127.0.0.1',port=1000,max_conn=10,logfile='fixedLeth.log')
variableServ = serv(host='127.0.0.1',port=2000,max_conn=10,logfile='variableLeth.log')
xmlServ = serv(host='127.0.0.1',port=3000,max_conn=10,logfile='xmlPrtcl.log')
fixedServ.importfunc(func=fixedfoo)
variableServ.importfunc(func=variableLethHelper)
fixedServ.run()

