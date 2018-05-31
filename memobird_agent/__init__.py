import base64
from PIL import Image
import io
import time
from .security import Encryption
import requests
from .config import CONFIG
import json

__version__ = CONFIG.VERSION
__all__ = ['Document']


class Document:
    def __init__(self):
        self.priority = 0
        self.textList = []

    def add_text(self, text="\n", bold=0, font_size=1, underline=0):
        if text.endswith("\n") is False:
            text += "\n"
        text = text.encode("gbk", 'replace')
        text = base64.b64encode(text).decode()
        self.textList.append(Document._new_print_item(text, bold, font_size, 1, underline))

    def add_qrcode(self, text="\n"):
        text += '\n'
        text = text.encode('gbk', 'replace')
        text = base64.b64encode(text).decode()
        self.textList.append(Document._new_print_item(text, print_type=3))

    def add_sticker(self, icon_id=0):
        self.textList.append(Document._new_print_item(icon_id=icon_id, print_type=4))

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

    def _generate_printing_content(self, smartGUID, userID, toUserID=0):
        toUserID = userID if toUserID == 0 else toUserID
        date = time.strftime("%Y-%m-%d %H:%M:%S")
        smartGUID = Encryption.encrypt_message(str(smartGUID), date)
        userID = Encryption.encrypt_message(str(userID), date)
        toUserID = Encryption.encrypt_message(str(toUserID), date)
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
                    "smartGuid": smartGUID,
                    "userId": userID,
                    "msgType": 1,
                    "packageNo": 1,
                    "command": 3,
                    "toUserId": toUserID,
                    "priority": 0
                },
                "datatype": "sendpaper"
            }
        }
        return {"msg": json.dumps(content)}

    def print(self, smartGUID, userID, toUserID=0):
        response = requests.post(CONFIG.URL,
                                 self._generate_printing_content(smartGUID, userID, toUserID))
        #TODO: Create decryped response and analyze it?
        return response.content.decode()
