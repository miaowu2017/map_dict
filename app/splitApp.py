#-*-coding:utf-8-*-
from mdlCmncatin.serv import serv
from getRetData import getRetData
from mdlLog.testLog import testLog
HOST = '127.0.0.1'
PORT = 1000
splitApp = serv(host=HOST,port=PORT,max_conn=10,logfile='splitApp.log')
def impTrxList():
    with open('TrxList.txt','rb') as listfile:
        trx = listfile.readlines()
        trx = map(lambda x:x.strip('\r\n'),trx)
        listfile.close()
    return trx
def splitfunc(clntsocket,trxcode):
    # 接收数据
    data = clntsocket.recv(1024)
    if data:
        print data
        testLog.write('splitApp.log','recv>'+data)
    # 返回数据
    try:
        retData = getRetData(trxcode,data)
        clntsocket.send(retData)
        testLog.write('splitApp.log', 'send>' + retData)
        #行号|交易码|社保号
        #行号|返回交易码|第三方返回码|返回社保号|姓名|征集金额
    except:
        pass
    clntsocket.close()
splitApp.importfunc(func=splitfunc)
# 82620 82621
trxcode = impTrxList()
splitApp.importtrxcode(trxcode=trxcode)
splitApp.run()