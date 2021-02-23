import re

amount_expression = int(input())
for expression in range(amount_expression):
    try:
        re.compile(input())
        print(True)
    except Exception:
        print(False)
