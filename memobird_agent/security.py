from Crypto.Cipher import DES
from Crypto.Util import Padding
from datetime import datetime
import hashlib
import base64


class Encryption:

    __primary_key = '4398f676'

    @staticmethod
    def decrypt_message(message, date):
        byteKey = Encryption.getDESKey(date).encode()
        w = DES.new(byteKey, DES.MODE_CBC, byteKey)

        message = base64.b64decode(message.replace("-", "+").encode())
        message = w.decrypt(message)
        message = Padding.unpad(message, 8, 'pkcs7').decode()
        return message

    @staticmethod
    def encrypt_message(message, date):
        byteKey = Encryption.getDESKey(date).encode()
        w = DES.new(byteKey, DES.MODE_CBC, byteKey)

        message = Padding.pad(message.encode(), 8, 'pkcs7')
        message = w.encrypt(message)
        message = base64.b64encode(message).decode().replace("+", "-")
        return message

    @staticmethod
    def getDESKey(date):
        try:
            time = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            time = datetime.strptime(date, '%Y/%m/%d %H:%M:%S')
        date = time.strftime('%Y%m%d%H%M%S')
        key = '4' + date[7:10] + '3' + date[8:11] + '9' + date[9:12] + '8' + date[10:13]+'f676'
        m = hashlib.md5()
        m.update(key.encode())
        key = m.hexdigest()[0:8]
        return key

