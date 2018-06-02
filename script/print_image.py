import sys
from memobird_agent import *

doc = Document()
doc.add_image(sys.argv[3])
print(doc.print(sys.argv[1], sys.argv[2], sys.argv[2]))
