# Enter your code here. Read input from STDIN. Print output to STDOUT
english_numbers = input()
english_students = set(map(int, input().split()))
french_numbers = input()
french_students = set(map(int, input().split()))

french_and_english = english_students.intersection(french_students)
print(len(french_and_english))
