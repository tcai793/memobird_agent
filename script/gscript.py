import sys
from memobird_agent import *
import memobird_agent
import zeep
import time
import json
import xml.etree.ElementTree as ET
import requests

doc = memobird_agent.Document()
doc.add_qrcode("测试")
doc.print("9da0ce0543c0f312", 22765)
