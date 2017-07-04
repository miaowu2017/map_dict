#-*-coding:utf-8-*-
import xml.dom.minidom
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
xh = xmlHelper("this_is_a_xml.xml")
print xh.getNodeAttribute(tagname="login",attr="username")
print xh.getNodeValue(tagname="caption",tagid=1)
