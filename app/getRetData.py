#-*-coding:utf-8-*-
from ConfigParser import ConfigParser

data_from_cosp = '11|1000|sb001'
trxcode = '82620'

def getRetData(trxcode,data_from_cosp):
    '''
    从cosp获取数据，并返回数据给gtcg
    :param data_from_cosp:
    :return:
    '''
    config = ConfigParser()
    config.read('partyRet.conf')
    recv = config.get(trxcode, 'recv')
    send = config.get(trxcode, 'send')
    options = config.options(trxcode)
    options.remove('recv')
    options.remove('send')
    # 获取含有类型标识符的粗数据
    options_raw_value = map(lambda x: config.get(trxcode, x), options)
    # 获取的cosp的数据
    def getData(raw_data):
        # raw_data:
        # 'index|0', 'index|1', 'value|00', 'index|2'
        data = raw_data.split('|')
        if data[0] == 'value':
            data = data[1]
        elif data[0] == 'index':
            data = data_from_cosp.split('|')[int(data[1])]
        return data

    options_value = map(getData, options_raw_value)
    return "|".join(options_value)
# test
# print getRetData(trxcode=trxcode,data_from_cosp=data_from_cosp)










