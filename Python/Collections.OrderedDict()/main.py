# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

number_items = int(input())
ordered_dictionary = OrderedDict()
for item in range(0, number_items):
    name_and_price = input()
    name_and_price = name_and_price.split()
    item_name = ' '.join(name_and_price[:-1])
    item_price = int(name_and_price[-1])
    if ordered_dictionary.get(item_name) == None:
        ordered_dictionary[item_name] = item_price
    else:
        ordered_dictionary[item_name] = item_price + ordered_dictionary[item_name]
for k, v in ordered_dictionary.items():
    print(k, v)
