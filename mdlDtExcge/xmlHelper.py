#-*-coding:utf-8-*-
import xml.dom.minidom
"""
revise - test at 2017-07-03
release 1.0
"""
class xmlHelper(object):
    root = ""
    def __init__(self,filename):
        self.root = xml.dom.minidom.parse(filename)
    def getNodeValue(self,tagname,tagid=0):
        tags = self.root.getElementsByTagName(tagname)
        return tags[tagid].firstChild.data
    def getNodeAttribute(self,tagname,attr,tagid = 0):
        tags = self.root.getElementsByTagName(tagname)
        return tags[tagid].getAttribute(attr)
    def getNodeValues(self,tagname):
        tags = self.root.getElementsByTagName(tagname)
        ids = range(0,len(tags))
        return map(lambda x:tags[x].firstChild.data,ids)