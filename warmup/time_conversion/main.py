# import os
# import sys
from datetime import datetime, time


#
# Complete the timeConversion function below.
#
def timeConversion(s):
    hour = s[0:2]
    minutes = s[3:5]
    seconds = s[6:8]
    am_pm = s[-2:]
    if am_pm == 'AM' and hour == '12':
        hour = '00'
    elif am_pm == 'PM' and hour != '12':
        hour = int(hour)
        hour += 12
    hour_24format = f'{hour}:{minutes}:{seconds}'
    return hour_24format

#######################
# if __name__ == '__main__':
#     f = open(os.environ['OUTPUT_PATH'], 'w')
#
#     s = input()
#
#     result = timeConversion(s)
#
#     f.write(result + '\n')
#
#     f.close()
