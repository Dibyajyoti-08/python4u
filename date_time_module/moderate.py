'''
Implement a function that calculates how many days are left 
until a given date (e.g., New Year).
'''

from datetime import datetime

def day_left_calculate(current_year):
    new_year_date =  datetime(current_year + 1, 1, 1).date()
    today_date = datetime.now().date()

    day_left = new_year_date - today_date
    print(f"Days left until New Year: {day_left.days}")

if __name__ == '__main__':
    day_left_calculate(2024)