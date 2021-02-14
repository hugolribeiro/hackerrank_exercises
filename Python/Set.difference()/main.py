# Enter your code here. Read input from STDIN. Print output to STDOUT
number_english = input()
english_students = set(input().split())
number_french = input()
french_students = set(input().split())
print(len(english_students.difference(french_students)))
