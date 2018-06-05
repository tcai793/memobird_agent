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