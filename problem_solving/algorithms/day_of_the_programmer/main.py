def dayOfProgrammer(year):
    if year >= 1919:
        date = greg_calendar(year)
    elif year != 1918 and (year != 1800 and year != 1900 and year != 1700):
        date = julian_calendar(year)
    elif year == 1800 or year == 1900 or year == 1700:
        date = f'12.09.{year}'
    elif year == 1918:
        date = f'26.09.1918'
    else:
        date = f'13.09.{year}'
    return date


def greg_calendar(year):
    leap_year = verify_leap(year)
    if leap_year:
        return f'12.09.{year}'
    else:
        return f'13.09.{year}'


def julian_calendar(year):
    leap_year = verify_leap(year)
    if leap_year:
        return f'12.09.{year}'
    else:
        return f'13.09.{year}'


def verify_leap(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    return False

print(dayOfProgrammer(1700))