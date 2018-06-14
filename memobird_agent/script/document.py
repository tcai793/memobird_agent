import memobird_agent
import datetime
import json

GENERAL_CONFIG_PATH = "/etc/memobird_agent/general.json"


class ReportDocument:
    def __init__(self):
        self._config = {}
        try:
            config_f = open(GENERAL_CONFIG_PATH)
            self._config = json.load(config_f)
            config_f.close()
        except:
            print("Error occurred when parsing general config file, exiting")
            exit(-1)
        if "smart_guid" not in self._config or "user_id" not in self._config or "machine_name" not in self._config:
            print("Machine config file missing item, exiting")
            exit(-1)
        # Change
        self._change = False
        # Document
        self._doc = memobird_agent.Document()
        self._doc.add_text("From: " + self._config["machine_name"])
        self._doc.add_text("Time: " + datetime.datetime.utcnow().strftime("%b %d %H:%M:%S"))
        self._doc.add_sticker(43)

    def add_text(self, text):
        self._change = True
        self._doc.add_text(text)

    def print(self):
        if self._change:
            self._doc.add_sticker(41)
            self._doc.print(self._config['smart_guid'], self._config["user_id"])
