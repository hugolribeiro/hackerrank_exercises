# Enter your code here. Read input from STDIN. Print output to STDOUT
number_english = int(input())
english_students = set(map(int, input().split()))
number_french = int(input())
french_students = set(map(int, input().split()))
print(len(english_students.union(french_students)))
