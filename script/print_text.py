import sys
from memobird_agent import *

argv = sys.argv[3:]
doc = Document()
for str in argv:
    doc.add_text(str)
print(doc.print(sys.argv[1], sys.argv[2], sys.argv[2]))
