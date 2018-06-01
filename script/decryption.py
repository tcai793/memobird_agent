import memobird_agent
import time
import sys

date = time.strftime("%Y-%m-%d %H:%M:%S")
str = "IAOK"
result = ''

for tmp in sys.stdin:
    tmp = tmp.replace("\n","").replace('"', '')
    try:
        time.strptime(tmp, "%Y-%m-%d %H:%M:%S")
        date = tmp
    except ValueError:
        str = tmp

    try:
        result = memobird_agent.Encryption.decrypt_message(str, date)
        print("Date:\t", date, "\nData:\t", str, "\nRslt:\t", result, "\n")
    except:
        print("Please check input:\nDate:\t", date, "\nData:\t", str, "\n")
