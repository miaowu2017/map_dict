#-*-coding:utf-8-*-
from ConfigParser import ConfigParser
from mdlDtExcge.xmlHelper import xmlHelper
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
    xhlp = xmlHelper()




