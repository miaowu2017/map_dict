#-*-coding:utf-8-*-
from mdlCmncatin.serv import serv
from getRetData import getRetData
HOST = '127.0.0.1'
PORT = 1000
splitApp = serv(host=HOST,port=PORT,max_conn=10,logfile='splitApp.log')
def splitfunc(clntsocket,trxcode):
    # 接收数据
    data = clntsocket.recv(1024)
    if data:
        print data
    # 返回数据
    try:
        retData = getRetData(trxcode,data)
        clntsocket.send(retData)
        #行号|交易码|社保号
        #行号|返回交易码|第三方返回码|返回社保号|姓名|征集金额
    except:
        pass
    clntsocket.close()
splitApp.importfunc(func=splitfunc)
# 82620 82621
splitApp.importtrxcode(trxcode='82621')
splitApp.run()