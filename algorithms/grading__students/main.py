# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#


def gradingStudents(grades):
    aut_list = []
    for grade in grades:
        if grade >= 38 and grade % 5 != 0:
            dif_next_multiple = 0
            check_grade = grade
            while check_grade % 5 != 0:
                check_grade += 1
                dif_next_multiple += 1
            if dif_next_multiple < 3:
                grade = check_grade
                aut_list.append(grade)
                continue
        aut_list.append(grade)
    return aut_list


#####################################
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     grades_count = int(input().strip())
#
#     grades = []
#
#     for _ in range(grades_count):
#         grades_item = int(input().strip())
#         grades.append(grades_item)
#
#     result = gradingStudents(grades)
#
#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')
#
#     fptr.close()
