#-*-coding:utf-8-*-
from ConfigParser import ConfigParser
import shelve
filename = ''
tagname = ''
digits = ''
fields_len = ''
fixed_blank = ''
fields_len = ''
fixed_blank = ''
leftfixed = ''
# '[ ,*,+]' ==> [' ','*','+']
def prcsit(str1):
    str1 = str1.lstrip('[')
    str1 = str1.rstrip(']')
    return str1.split(',')
def getConfig():
    cfg = ConfigParser()
    cfg.read('./params.ini')
    # xml
    global filename,tagname,digits,fixed_blank,leftfixed,fields_len
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
    leftfixed = bool(cfg.get('FIXED','leftfixed'))
    config = shelve.open("config")
    params = {'filename':filename,'tagname':tagname,'digits':digits,'fields_len':fields_len\
              ,'fixed_blank':fixed_blank,'leftfixed':leftfixed}
    config['params'] = params
    config.close()
def printConfig():
    #print config
    print 'config list'
    print '-'*30
    print 'xml:'
    print '\tfilename:',filename
    print '\ttagname:',tagname
    print 'variable:'
    print '\tdigits:',digits
    print 'fixed:'
    print '\tfields_len:',fields_len
    print '\tfixed_blank:',fixed_blank
    print '\tleftfixed:',bool(leftfixed)
if __name__ == '__main__':
    getConfig()
    # printConfig()