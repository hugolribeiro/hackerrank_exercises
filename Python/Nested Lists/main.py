if __name__ == '__main__':
    python_students = []
    lowest_score = second_lowest_score = 99999999999999
    for _ in range(int(input())):
        name = input()
        score = float(input())
        python_students.append([name, score])
        if score < lowest_score:
            second_lowest_score = lowest_score
            lowest_score = score
        elif score < second_lowest_score and score != lowest_score:
            second_lowest_score = score
    second_lowest_scores = []
    for student in python_students:
        if student[1] == second_lowest_score:
            second_lowest_scores.append(student)
    sorted_second_lowest = sorted(second_lowest_scores, key = lambda x : x[0])
    for student in sorted_second_lowest:
        print(student[0])
        
