'''
Write a program that takes two dates and 
calculates the number of days between them
'''

from datetime import datetime

def date_diff(date1_str, date2_str):
    date_format = "%Y-%m-%d"

    date1 = datetime.strptime(date1_str, date_format).date()
    date2 = datetime.strptime(date2_str, date_format).date()

    difference = (date2 - date1).days
    print(f"The difference between two date is {difference}")

if __name__ == '__main__':
    date_diff("2024-09-26", "2024-09-28")