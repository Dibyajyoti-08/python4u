'''
Write a Python script to print today’s date and time.
'''

from datetime import datetime

def current_timeline():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Todays date and time in India: {current_time}")

if __name__ == '__main__':
    current_timeline()
