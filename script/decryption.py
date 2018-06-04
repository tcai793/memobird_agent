import memobird_agent
import time
import sys

date = time.strftime("%Y-%m-%d %H:%M:%S")
string = 'IA0K'
result = ''

for tmp in sys.stdin:
    tmp = tmp.replace("\n", "").replace(' "', "").replace('" ', "").replace('"', '')
    try:
        time.strptime(tmp, "%Y-%m-%d %H:%M:%S")
        date = tmp
    except ValueError:
        string = tmp

    try:
        result = memobird_agent.Encryption.decrypt_message(string, date)
        print("Date:\t", date, "\nData:\t", string, "\nRslt:\t", result, "\n")
    except:
        print("Please check input:\nDate:\t", date, "\nData:\t", string, "\n")
