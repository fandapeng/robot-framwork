# -*- coding: utf-8 -*-


from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
import time
import random
import string
import pymysql
import os
import base64,json
from pyDes import *

class Common_Function(object):

    def __init__(self):

        self._builtin = BuiltIn()
        self._fake = Faker('zh_CN')
        self.key = "1qaz!@#$"
        self.iv = "\x01\x02\x03\x04\x05\x06\x07\x08"
        self.k = des(self.key, CBC, self.iv, pad=None, padmode=PAD_PKCS5)
        self.key2 = "cf410f84904a44cc8a7f48fc4134e8f9"[:24]
        self.k2 = triple_des(self.key2, ECB, padmode=PAD_PKCS5)

    def create_request_id(self):
        """
        随机生成requestId\n
        固定字符串APIAutoTest+13位时间戳+6位随机数，构成30位requestId

        示例：
        | ${reqid} | Create Request Id |
        """
        return "APIAutoTest"+str(int(round(time.time()*1000)))+str(random.randint(100, 999))

    def create_phone(self):
        try:
            with open('phone.txt', 'r') as f:
                oldphone=int(f.readline())

            newphone=str(oldphone+1)
            with open('phone.txt', 'w') as f:            
                f.write(newphone)
        except:
            newphone = str(int(time.time()*10)+100000000)
            # newphone = str(188)+''.join(str(i) for i in random.sample(range(0,9),8))


        return newphone

    def create_bank_info(self,bankname):

        bankcard_suffix = ''.join(random.sample(string.digits * 10, 11))

        if bankname == u'中国工商银行':
            bankcard_prefix = '622202'
            bankcard_credit = '622231'
            bankcode = 'ICBC'
            # reqUuid = random.sample(string.letters,6)+random.sample(string.digits,13)
            # random.shuffle(reqUuid)
            # reqUuid = ''.join(reqUuid)
            reqUuid = ''.join(random.sample(string.letters, 6) + random.sample(string.digits, 10))
        if bankname==u'中国银行':
            bankcard_prefix  = '621790'
            bankcode='BOC' 
        if bankname==u'中国农业银行':
            bankcard_prefix  = '622848'
            bankcode='ABC'

        return bankcard_prefix + bankcard_suffix + '0',bankcard_prefix + bankcard_suffix + '10',\
               bankcard_credit + bankcard_suffix, bankcode, bankname, reqUuid

    def create_account_info(self,bankname=u'中国工商银行'):
        """
        生成一个用户的基本信息信息,包含：姓名，身份证，手机号码，银行卡，银行

        示例：
        | ${account_info} | Create Account Info |
        | ${account_info} | Create Account Info | 中国银行 |
        """
        person=self._fake.profile(fields=('name','ssn'), sex=None)
        person['ssn'] = self._fake.ssn(min_age=20, max_age=45)
        person['phone']=self.create_phone()
        person['bankcard'],person['bankcardNo'], person['bankcard_credit'], person['bankcode'], person['bankname'], person[
            'reqUuid'] = self.create_bank_info(bankname)

        print person
        return person

    def create_newfile(self):
        """
        每次生成不同的文件名，内容写死

        示例：
        | ${account_info} | Create newfile |

        """
        num = random.randint(1, 10000000)
        lastname = "hx_ftp_" + str(num) + ".txt"
        document = open(lastname, "w+")
        document.write("a\nb\nc\n")
        document.close()


    def des_encrypt(self, str):
        """
        des加密方法

        示例：
        | ${data} | Des Encrypt | aaaaaaaa |

        """
        
        return base64.b64encode(self.k.encrypt(str.encode("utf-8")))



    def des_decrypt(self, str):
        return self.k.decrypt(base64.b64decode(str))

    def three_des_encrypt(self, str):
        """
        3des加密，适用于各要素加密

        示例：
        | ${data} | Three Des Encrypt | aaaaaaaa |

        """
        return base64.b64encode(self.k2.encrypt(str))


    def three_des_decrypt(self, str):
        """
        3des加密，适用于各要素解密

        示例：
        | ${data} | Three Des Decrypt | aaaaaaaa |

        """
        return self.k2.decrypt(base64.b64decode(str))

    # def member_fee(self,on_off):
    #     '''
    #     开关，如果为ON，则为打开会员费，如果为OFF，则去除会员费选项
    #     '''
    #     if on_off == "ON":
    #         price = json['result']['price']
    #     elif on_off == "OFF":
    #         pass


if __name__ == '__main__':
    a = Common_Function()
    a.create_account_info()
    # a.create_newfile()
    # print len(a.create_request_id())
    # print a.des_decrypt("Kme5ZuXvxxg=")




