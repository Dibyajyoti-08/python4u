'''
Implement a function that prints the current time in another time zone (e.g., UTC).
'''

from datetime import datetime
from datetime import timezone

def utc_timezone():
    current_loc_time = datetime.now().time()
    utc_time = datetime.now(timezone.utc).time()
    print(f"Current time in your location: {current_loc_time}")
    print(f"Current time in UTC timezone: {utc_time}")

if __name__ == '__main__':
    utc_timezone()