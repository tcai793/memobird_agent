import sys
from memobird_agent import *

for i in range(0, 7):
    doc = Document()
    for j in range(1, 11):
        doc.add_text(i * 10 + j)
        doc.add_sticker(i * 10 + j)
    print(doc.print(sys.argv[1], sys.argv[2], sys.argv[2]))
