'''
Create a script that takes a date in the format "dd-mm-yyyy" as input, 
converts it to a datetime object, and prints how many weeks have passed 
since that date.
'''

from datetime import datetime

def week_since(date_str):
    date_format = "%d-%m-%Y"

    input_date = datetime.strptime(date_str, date_format)

    current_date = datetime.now()

    days_diff = (current_date - input_date).days

    week_passed = days_diff // 7

    return week_passed

if __name__ == '__main__':
    date_input = input("Enter a date dd-mm-yyyy: ")
    weeks = week_since(date_input)
    print(f"Weeks passed since {date_input}: {weeks} weeks")