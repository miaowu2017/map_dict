#-*-coding:utf-8-*-
class fixedLethHelper(object):
    fields_len = []
    leftfixed = False
    def __init__(self,fields_len,fixed_blank,leftfixed=False):
        """

        :param fields_len:lenght of each field
        :param fixed_blank: fixed char of each field
        :param leftfixed: fixed position of the content
        """
        self.fields_len = fields_len
        self.leftfixed = leftfixed
        self.fixed_blank = fixed_blank
        if len(self.fields_len)!=len(self.fixed_blank):
            raise Exception("reset fixed_blank or fields_len , the len of the two must be same")
    def pack(self,data):
        data_result = ""
        if len(data)!=len(self.fields_len):
            raise Exception("len of fields must be same with data")
        for i in range(0,len(self.fields_len)):
            current_data = data[i]
            current_data_len = len(current_data)
            current_fixed_len = self.fields_len[i]
            if current_data_len > current_fixed_len:
                raise Exception("len above the fixed lenght")
            elif current_data_len == current_fixed_len:
                data_result+=data[i]
            else:
                if self.leftfixed:
                    data_result+=self.fixed_blank[i]*(current_fixed_len-current_data_len)+data[i]
                else:
                    data_result +=data[i]+self.fixed_blank[i] * (current_fixed_len - current_data_len)
        return data_result

    def unpack(self,str1):
        data_result = []
        i = 0
        j = 0
        while i < len(self.fields_len):
            current_len = self.fields_len[i]
            current_dat = str1[j:j + current_len]
            data_result.append(current_dat)
            i += 1
            j += current_len
        return tuple(data_result)
#e.g
fh = fixedLethHelper(leftfixed=False,fields_len=[3,5,10],fixed_blank=['0','0','*'])
str1 =  fh.pack(['01','0001',u'中国'])
data = fh.unpack(str1)
print data
for i in range(len(data)):
    print data[i]
