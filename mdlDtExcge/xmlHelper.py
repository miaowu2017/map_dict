#-*-coding:utf-8-*-
import xml.dom.minidom
import shelve
slv = shelve.open('../mdlConfig/config')
params = slv['params']
slv.close()
class xmlHelper(object):
    root = ""
    def __init__(self,filename=params['filename']):
        self.root = xml.dom.minidom.parse(filename)
    def getNodeValue(self,tagname=params['tagname'],tagid=0):
        tags = self.root.getElementsByTagName(tagname)
        return tags[tagid].firstChild.data
    def getNodeAttribute(self,attr,tagname=params['tagname'],tagid = 0):
        tags = self.root.getElementsByTagName(tagname)
        return tags[tagid].getAttribute(attr)
    def getNodeValues(self,tagname=params['tagname']):
        tags = self.root.getElementsByTagName(tagname)
        ids = range(0,len(tags))
        return map(lambda x:tags[x].firstChild.data,ids)