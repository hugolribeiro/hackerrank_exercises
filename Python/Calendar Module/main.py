# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

days_week = {
    0: 'MONDAY',
    1: 'TUESDAY',
    2: 'WEDNESDAY',
    3: 'THURSDAY',
    4: 'FRIDAY',
    5: 'SATURDAY',
    6: 'SUNDAY'
}

full_data = input().split(' ')
year = int(full_data[2])
month = int(full_data[0])
day = int(full_data[1])

print(days_week[(calendar.weekday(year, month, day))])
