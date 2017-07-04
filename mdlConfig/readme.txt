目的及内容:此文件夹主要管理是报文的配置参数信息
报文类型认知： 报文格式：xml 、定长报文、变长报文
处理思路:使用python可以轻松处理定长报文和变长报文格式
处理xml需要使用现成已经开发的库
对应处理定长报文和报文格式，python可以说是得心应手
但需要对定长报文做配置化处理
xml例子：
<?xml version="1.0" encoding="utf-8"?>
<catalog>
    <maxid>4</maxid>
    <login username="pytest" passwd='123456'>
        <caption>Python</caption>
        <item id="4">
            <caption>测试</caption>
        </item>
    </login>
    <item id="2">
        <caption>Zope</caption>
    </item>
</catalog>

更新：
1、新建trades文件夹，专门放交易的配置文件