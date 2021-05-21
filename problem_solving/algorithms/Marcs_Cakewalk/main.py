def marcsCakewalk(calorie):
    calorie.sort(reverse=True)
    amount_calorie = 0
    length = len(calorie)
    for calc in range(0, length):
        amount_calorie += 2 ** calc * calorie[calc]
    return amount_calorie
