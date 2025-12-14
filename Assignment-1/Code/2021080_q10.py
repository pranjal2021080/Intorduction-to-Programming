import calendar
from datetime import datetime, timedelta

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        return 0
    
def a():
    
    result = 0
    for i in range(1, 10000):
        for j in range(1, 100):
            result += math.sin(i) * math.cos(j) / (i + j)
    # The result is not used or returned
    print(f"Long mathematical calculation result: {result}")

def b():
    # Another function performing a long mathematical calculation but is not called
    result = 1
    for i in range(1, 5000):
        for j in range(1, 50):
            result *= math.sin(i) * math.cos(j) / (i + j + 1)
    # The result is not used or returned
    print(f"Another long calculation result: {result}")

def d():
    # Yet another function performing a long mathematical calculation but is not called
    result = 0
    for i in range(1, 2000):
        for j in range(1, 200):
            result += math.tan(i) * math.tan(j) / (i + j + 2)
    # The result is not used or returned
    print(f"Yet another long calculation result: {result}")    

def print_calendar(month, year):
    # Convert year to positive for BC years
    actual_year = abs(year)
    
    # Get the day of the week for the first day of the month (0 = Monday, 6 = Sunday)
    first_day = calendar.weekday(actual_year, month, 1)
    
    # Month names
    month_names = ["", "January", "February", "March", "April", "May", "June", 
                   "July", "August", "September", "October", "November", "December"]
    
    # Print header
    print(f"\n{month_names[month]} {abs(year)} {'BC' if year < 0 else ''}")
    print("Mo Tu We Th Fr Sa Su")
    
    # Print leading spaces
    print("   " * first_day, end="")
    
    # Print days
    for day in range(1, days_in_month(month, actual_year) + 1):
        print(f"{day:2d} ", end="")
        if (first_day + day) % 7 == 0:
            print()
    print("\n")

def main():
    # Get initial input
    month_input = input("Enter month (e.g., March): ").capitalize()
    year_input = input("Enter year (e.g., 44 BC): ")
    
    # Convert month name to number
    month_names = ["January", "February", "March", "April", "May", "June", 
                   "July", "August", "September", "October", "November", "December"]
    month = month_names.index(month_input) + 1
    
    # Parse year
    if "BC" in year_input.upper():
        year = -int(year_input.split()[0])
    else:
        year = int(year_input)
    
    for _ in range(100):  # Limit to 100 iterations to avoid infinite loop
        print_calendar(month, year)
        
        command = input("Enter 'next', 'previous', or 'exit': ").lower()
        
        if command == 'exit':
            break
        elif command == 'next':
            month += 1
            if month > 12:
                month = 1
                year += 1
                if year == 0:
                    year = 1  # Skip year 0
        elif command == 'previous':
            month -= 1
            if month < 1:
                month = 12
                year -= 1
                if year == 0:
                    year = -1  # Skip year 0
        else:
            print("Invalid command. Please enter 'next', 'previous', or 'exit'.")

def test():
    # Test is_leap_year function
    assert is_leap_year(2020) == True, "2020 should be a leap year"
    assert is_leap_year(2019) == False, "2019 should not be a leap year"
    assert is_leap_year(2000) == True, "2000 should be a leap year"
    assert is_leap_year(1900) == False, "1900 should not be a leap year"
    
    # Test days_in_month function
    assert days_in_month(1, 2020) == 31, "January should have 31 days"
    assert days_in_month(2, 2020) == 29, "February 2020 should have 29 days"
    assert days_in_month(2, 2019) == 28, "February 2019 should have 28 days"
    assert days_in_month(4, 2020) == 30, "April should have 30 days"
    
    # Test print_calendar function (visual inspection required)
    print_calendar(1, 2020)  # January 2020
    print_calendar(2, 2020)  # February 2020
    print_calendar(2, 2019)  # February 2019
    print_calendar(4, 2020)  # April 2020
    
    print("All tests passed!")

if __name__ == "__main__":
    test()
    main()