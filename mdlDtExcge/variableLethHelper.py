#-*-coding:utf-8-*-
class variableLethHelper(object):
    digits = 3
    def __init__(self,digits):
        """
        :param digits:每个字段前面digits位表示变长长度的意思
        """
        self.digits = digits
    def pack(self,data):
        """
        对data数据进行拆包处理
        :param data:
        :return:
        """
        res_str = ""
        for i in range(len(data)):
            res_str+="%0{}d".format(self.digits)%len(str(data[i]))+str(data[i])
        return res_str

    def unpack(self,str1):
        res_data = []
        i = 0
        while i <len(str1):
            field_len = int(str1[i:i+int(self.digits)])
            i = i + int(self.digits)
            field_value = str1[i:i+int(field_len)]
            i = i + int(field_len)
            res_data.append(field_value)
        return res_data
def test():
    return variableLethHelper(digits=3).pack([1,2,"中国"])

def test2(str1):
    return variableLethHelper(digits=3).unpack(str1)

# print test()
# for each in test2('00110012006中国'):
#     print each