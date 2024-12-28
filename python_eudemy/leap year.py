def leap_year(y):
    if y % 4 == 0 and y % 100 == 0 and y % 400 == 0:
        return True
    else:
        return False


def days_in_month(y, m):
    x = leap_year(y)
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if x == True:
        if m == 2:
            return month_days[m - 1] + 1
        else:
            return month_days[m - 1]
    else:
        return month_days[m - 1]


year = int(input("enter the year: "))
month = int(input("enter the month: "))
total_days = days_in_month(year, month)
print(f"No. of days in month is = {total_days}")



#2nd approach:-
'''def leap_year(y):
    if y % 4 == 0 and y % 100 == 0 and y % 400 == 0:
        return True
    else:
        return False


def days_in_month(y, m):
    x = leap_year(y)
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if x == True and m==2:
        return 29
    return month_days[m-1]
year = int(input("enter the year: "))
month = int(input("enter the month: "))
total_days = days_in_month(year, month)
print(f"No. of days in month is = {total_days}")
'''