#-*-coding:utf-8-*-
"""
testLog.py --- 日志记录类，用于记录测试日志
"""
from time import ctime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class testLog(object):
    @staticmethod
    def write(logfilename,data):
        with open(logfilename,'a') as logfile:
            logfile.write('[%s]'%ctime())
            logfile.write(data)
            logfile.write('\n')
            logfile.close()
# testLog.write("test.log",'你好么?')
