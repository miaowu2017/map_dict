#-*-coding:utf-8-*-
from ConfigParser import ConfigParser
from mdlDtExcge.xmlHelper import xmlHelper
from mdlDtExcge.fixedLethHelper import fixedLethHelper
from mdlDtExcge.variableLethHelper import variableLethHelper
# '[ ,*,+]' ==> [' ','*','+']
def prcsit(str1):
    str1 = str1.lstrip('[')
    str1 = str1.rstrip(']')
    return str1.split(',')
cfg = ConfigParser()
cfg.read('params.ini')
# xml
filename = cfg.get('XML','filename')
tagname = cfg.get('XML','tagname')
tagname = prcsit(tagname)
# variable
digits = cfg.get('VARIABLE','digits')
# fixed
fields_len = cfg.get('FIXED','fields_len')
fixed_blank = cfg.get('FIXED','fixed_blank')
fields_len = prcsit(fields_len)
fixed_blank = prcsit(fixed_blank)
leftfixed = cfg.get('FIXED','leftfixed')

print filename
print tagname
print digits
print fields_len
print fixed_blank
print leftfixed

def parseXML():
    xhlp = xmlHelper(filename=filename)
    return map(lambda x:xhlp.getNodeValues(tagname=x),tagname)

print '-'*20
print tagname[0]
for name in parseXML()[0]:
    print name
print '-'*20
print tagname[1]
for acc in parseXML()[1]:
    print acc
print '-'*20
print tagname[2]
for balance in parseXML()[2]:
    print balance
print '-'*20


def parseFixed():
    # print 'enter a fixed protocol'
    str1 = 'abc123def'
    print str1
    fhlp = fixedLethHelper(fields_len=fields_len,fixed_blank=fixed_blank,leftfixed=bool(leftfixed))
    print fhlp.unpack(str1=str1)

parseFixed()


def parseVariable():
    # print 'enter a variable protocol'
    # str1 = raw_input('>')
    str1 = '001a002ab003abc'
    print str1
    vhlp =variableLethHelper(digits=digits)
    print vhlp.unpack(str1)


parseVariable()




