# Enter your code here. Read input from STDIN. Print output to STDOUT
students, subjects = input().split(' ')
all_scores = []
for subject in range(0, int(subjects)):
    all_scores.append(map(float, list(input().split(' '))))

zipped = list(zip(*all_scores))

for student in zipped:
    print((sum(student)) / (len(student)))

