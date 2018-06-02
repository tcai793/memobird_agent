import memobird_agent
import time
import sys

date = time.strftime("%Y-%m-%d %H:%M:%S")
string = 'tLdm2fETDvUvHksYiFCiwLba0YiLl3TCPCzNy+fzjWitlZThhtu80jt2WBkzqdQXW06NVJoC2quMEOIJwPov7tU09pMh+sG3XHKdGy+y6+GfjuelkYBmitwto0KYeadAkvzJYTDWRoT/YcJwSzBhl+TCsFPt0y3CeLQ/MkXvVnGqgOzocybfxwav2TxSb6Lg9XEraMapj4BQNJzsy12FNShPCB6P57yILGPJLqjbICU6cJjF2UrX4GGU0gnkDi7e34s2D7Ef+wo+B/vQe2tWdT4y5TQckuFQwFAOMhVsIJmY/XNQMFpPOIUsoHl8JDVqZkZZPrAuSW3RV3GWpbxPMp+/6zvDX/6UpnBBw6n4PTFqFaanIjA+YGgDaQ/p9uRxviWLKbWoPlqQOyQgAas4PWLRDOFED/Y/aOyk+fWmMKrwzTXVoIHggORPHQnK+Zp21O70CjpQSq3X7eisrSMJW15kyPrwmA61MHIERz1rYpm/K7WKQsVSmUZWIxJJWcdsEjABUUZFF80PsmKd+cE+1OXxtqqGSn3sMW4I8bYviATWqoeNugfmWBr9c3wEH6BZanwHsjKiPNxTnQKO6mkZec4NdZEHNSva4q01sdb+OUsRhOi6PowfQMeN0Ml0RQX9j3zEgrsG8IUNURp9w2JfQrFLm2Nj7HBbvYGXgFwPPrL6+FIvQbrHeJM97PMK4TJLHYa1zDwUE6SujtMV7z04ZtTYJ+qktHC3FTooCM1Q30bTz0Fv0tGDKMTXB9YqLNuIxMwTyKEUKOuRiU6amIuFfyg/vyKwHvkF'
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
