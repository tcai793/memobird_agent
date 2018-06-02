import base64
from PIL import Image
import io
import time
from .security import Encryption
import requests
from .config import CONFIG
import json
import xml.etree.ElementTree as ET

__version__ = CONFIG.VERSION
__all__ = ['Document', 'Util']


class Document:
    def __init__(self):
        self.priority = 0
        self.textList = []

    def add_text(self, text="\n", bold=0, font_size=1, underline=0):
        text = str(text)
        bold = int(bold)
        font_size = int(font_size)
        underline = int(underline)
        if text.endswith("\n") is False:
            text += "\n"
        text = text.encode("gbk", 'replace')
        text = base64.b64encode(text).decode()
        self.textList.append(Document._new_print_item(text, bold, font_size, 0, 1, underline))

    def add_qrcode(self, text="\n"):
        text = str(text)
        if text.endswith("\n") is False:
            text += '\n'
        text = text.encode()
        text = base64.b64encode(text).decode()
        self.textList.append(Document._new_print_item(text, print_type=3))

    def add_sticker(self, sticker_id=0):
        sticker_id = int(sticker_id)
        self.textList.append(Document._new_print_item(icon_id=sticker_id, print_type=4))

    def add_picture(self, path):
        image = Image.open(path)
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
        if image.width > 384:
            image = image.resize((384, image.height * 384 // image.width), Image.LANCZOS)
        image = image.convert('1')
        image_byte_array = io.BytesIO()
        image.save(image_byte_array, "BMP")
        image_byte_array = base64.b64encode(image_byte_array.getvalue()).decode()
        self.textList.append(Document._new_print_item(image_byte_array, print_type=5))

    def set_important(self):
        self.priority = 1

    @staticmethod
    def _new_print_item(base_text="IA0K", bold=0, font_size=1, icon_id=0, print_type=1, underline=0):
        return {
            "basetext": base_text,
            "bold": bold,
            "fontSize": font_size,
            "iconID": icon_id,
            "printType": print_type,
            "underline": underline
        }

    def _generate_printing_content(self, smart_guid, user_id, to_user_id=0):
        to_user_id = user_id if to_user_id == 0 else to_user_id
        date = time.strftime("%Y-%m-%d %H:%M:%S")
        smart_guid = Encryption.encrypt_message(str(smart_guid), date)
        user_id = Encryption.encrypt_message(str(user_id), date)
        to_user_id = Encryption.encrypt_message(str(to_user_id), date)
        content = {
            "type": "1",
            "sysDate": date,
            "parameter": {
                "content": {
                    "strDate": date,
                    "content": {
                        "textList": self.textList
                    },
                    "result": 0,
                    "packageCount": 1,
                    "smartGuid": smart_guid,
                    "userId": user_id,
                    "msgType": 1,
                    "packageNo": 1,
                    "command": 3,
                    "toUserId": to_user_id,
                    "priority": 0
                },
                "datatype": "sendpaper"
            }
        }
        return {"msg": json.dumps(content)}

    # returns (code, print_content_id). code is 0 if syntax error occur; 1 if stored in db; 2 if send to machine
    def print(self, smart_guid, user_id, to_user_id=0):
        user_id = int(user_id)
        to_user_id = int(to_user_id)
        print_content = self._generate_printing_content(smart_guid, user_id, to_user_id)
        response = Connection.send_print_command(print_content)
        return response


class Util:
    @staticmethod
    # returns userID if success, else return -1
    def get_user_id(username, password):
        username = str(username)
        password = str(password)
        login_parameter = CONFIG.LOGIN_MESSAGE_TEMPLATE.replace("USERNAME", username).replace("PASSWORD", password)
        result = Connection.send_util_command(login_parameter, "Login")
        if result['code'] is not 1:
            return -1
        return result['user']['userId']

    @staticmethod
    # returns 1 if success, else return -1
    def bind_machine(smart_guid, user_id):
        smart_guid = str(smart_guid)
        user_id = str(user_id)
        parameter = CONFIG.BIND_MACHINE_MESSAGE_TEMPLATE.replace("GUID", smart_guid).replace("USERID", user_id)
        result = Connection.send_util_command(parameter, "ActivationXG")
        if result['code'] is not 1:
            return -1
        return 1

    @staticmethod
    def set_led_buzz_status(buzz, led):
        obj = {
            "buz": "0",
            "smartguid": "",
            "led": "1",
            "speed": "15",
            "datatype": "setbuzled"
        }
        pass


class Connection:
    @staticmethod
    # returns (code, print_content_id). code is 0 if syntax error occur; 1 if stored in db; 2 if send to machine
    def send_print_command(printing_content):
        ret_code = 0
        content_id = None
        response = requests.post(CONFIG.PRINT_URL, printing_content)
        encoded_json = response.content.decode()
        if encoded_json == '参数错误':
            return ret_code, content_id
        json_result = json.loads(encoded_json)
        decrypted_result = json.loads(Encryption.decrypt_message(json_result['data'], json_result['sysDate']))
        return decrypted_result['code'], decrypted_result['PrintContentID']

    @staticmethod
    def send_util_command(parameter, operation):
        date = time.strftime("%Y-%m-%d %H:%M:%S")
        encrypted_parameter = Encryption.encrypt_message(parameter, date)
        message = json.dumps({'sysDate': date, 'parameter': encrypted_parameter})
        send_xml = CONFIG.XML_TEMPLATE.replace("MESSAGE", message).replace("OPERATION", operation)
        response = requests.post(CONFIG.APP_URL, send_xml,
                                 headers=json.loads(CONFIG.SOAP_HEADER.replace("OPERATION", operation)))
        result_xml = ET.fromstring(response.content.decode())

        xml_locator = CONFIG.XML_RESPONSE_LOCATOR.replace("OPERATION", operation)
        encoded_json = json.loads(result_xml.find(xml_locator).text)
        json_result = json.loads(Encryption.decrypt_message(encoded_json['data'], encoded_json['sysDate']))
        return json_result
