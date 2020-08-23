import hashlib
import base64

#密码的加解密类：用于字符串的加密和解密

class StringEncrypt():
      #MD5加密
    def md5Encrypt(self,string):
        md5Object=hashlib.md5()
        md5Object.update(string.encode(encoding='utf-8'))
        md5String=md5Object.hexdigest()
        return md5String

     #base64加密
    def base64Encrypt(self,string):
        bs=base64.b64encode(string.encode('utf8')).decode()  #解码城字符串，python默认是unicode码
        return bs

     #base64解密
    def base64Decrypt(self,string):
        string=base64.b64decode(string)
        bs=string.decode('utf8')
        return bs

if __name__=='__main__':
    text1=StringEncrypt().md5Encrypt('Sheng123456@@')
    print("MD5加密后:%s"%text1)
    text2=StringEncrypt().base64Encrypt('Sheng123456@@')
    print("Base64加密后:%s"%text2)
    text3=StringEncrypt().base64Decrypt(text2)
    print("Base64解密后:%s"%text3)
