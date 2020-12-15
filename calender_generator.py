import colorama
from colorama import *

def print_month_name(year, month):
    """Prints name of the month and weeks"""

    print('\033[1m' + f"           {get_month_name(month)}" + Style.RESET_ALL)
    print("————————————————————————————") 
    print(Back.WHITE + " Sun" + Style.RESET_ALL + Back.BLACK + Fore.WHITE + " Mon Tue Wed Thu Fri" + Style.RESET_ALL + Back.WHITE + " Sat" + Style.RESET_ALL)

def get_month_name(month_num):
    """Checks for months and assign a month name"""
    MONTHS = {
            1: 'January',
            2: 'February',
            3: 'March',
            4: 'April',
            5: 'May',
            6: 'June',
            7: 'July',
            8: 'August',
            9: 'September',
            10: 'October',
            11: 'November',
            12: 'December'
    }
    month = MONTHS[month_num]

    if month_num  in [3,4,5]:
        month = Fore.GREEN + month + Style.RESET_ALL
    elif month_num in [6,7,8]:
        month = Fore.YELLOW + month + Style.RESET_ALL
    elif month_num in [9,10,11]:
        month = Fore.RED + month + Style.RESET_ALL 
    else: 
        month = Fore.BLUE + month + Style.RESET_ALL 
    return month 

def print_month_body(year, month):
    """Prints the month in the year"""

    start_day = get_start_day(year, month)
    get_month = get_days_month(year, month)

    for i in range(0, start_day):
        print("   ", end=" ")

    for i in range(1, get_month + 1):
        print(format(i, "4d"), end ="")

        if (i + start_day) % 7 == 0:
            print()
    print()   

def print_month(year, month):
    """Prints the full calendar for a month"""

    print_month_name(year, month)
    print_month_body(year, month)


def get_start_day(year, month):
    """Gets the start day of the month in the year"""

    START_DAY_JAN_1900 = 1

    total_days = get_total_days(year, month)
    days_month = total_days + START_DAY_JAN_1900

    return days_month % 7


def get_total_days(year,month):
    """Gets the total days in the month"""

    total = 0

    for y in range(1900, year):
        if check_leap_year(year):
            total += 366
        else:
            total += 365

    for m in range(1, month):
        total += get_days_month(year, m)

    return total

def get_days_month(year,month):
    """Gets the number of days in a month"""

    month_days_31 = [1, 3, 5, 7, 8, 10, 12]
    month_days_30 = [4, 6, 9, 11]
    
    if month in month_days_31:
        return 31
    elif month in month_days_30:
        return 30
    elif month == 2:
        if check_leap_year(year):
            return 29
        else:
            return 28
    else:
        return 0

def check_leap_year(year):
    """checks if its a leap year"""

    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return year

def check_valid_year(year):
    """Checks if user has a valid input for year"""

    if year >= 1900:
        return True
    else:
        print("Please enter a valid year!")
        return False

def check_valid_month(month):
    """Checks if user has a valid month for month"""

    if month in range(1, 13):
        return True
    else:
        print("Please enter a valid month!")
        return False

def display_calender():
    """Prints messages on the screen and prints the calender"""

    print('\033[1m' + "Welcome to the Calendar Generator program!" + Style.RESET_ALL)
    print('\033[1m' + "Calendar Generator since 1900" + Style.RESET_ALL)
    
    

def main():
    """Runs the program"""
    display_calender()
    
    while True:
        year = int(input("Please enter the year (yyyy): "))
        month = int(input("Please enter the month (mm): "))
        print()

        if not check_valid_year(year):
            continue

        if not check_valid_month(month):
            continue

        print_month(year, month)
        print()

        check = input("You want to continue(Y/N)? ")

        if check.lower() == 'n':
            print("Thank you for using our Calendar Generator!")
            break
    
main()
