import sys
from memobird_agent import *

argv = sys.argv[3:]
doc = Document()
for s in argv:
    doc.add_text(s)
print(doc.print(sys.argv[1], sys.argv[2], sys.argv[2]))
