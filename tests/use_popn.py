#-*-coding:utf-8-*-
import os
p=os.popen('type clnt.log')
print p.read().decode('gbk').split('\n')
with open("clnt.log",'wr') as file:
    file.read()
    file.write('sw')
    file.close