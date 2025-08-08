'''1. Write a program that converts a list of tuples into a dictionary.
Example: [('a', 1), ('b', 2)] → {'a': 1, 'b': 2}'''


n = int(input("Enter number of tuples: "))
tuple_list = []

for i in range(n):
    key = input(f"Enter key for tuple {i+1}: ")
    value = input(f"Enter value for tuple {i+1}: ")
    tuple_list.append((key, value))

result_dict = dict(tuple_list)
print("Converted Dictionary:", result_dict)

'''2. Given a dictionary with values as lists, write a program to flatten all values into a single
list.'''


n = int(input("Enter number of keys: "))
dict_of_lists = dict()

for i in range(n):
    key = input(f"Enter key {i+1}: ")
    values = input(f"Enter values for {key} (space separated): ").split()
    dict_of_lists[key] = values

flattened_list = []
for value_list in dict_of_lists.values():
    for value in value_list:
        flattened_list.append(value)

print("Flattened List:", flattened_list)

'''3. Write a program that takes a list with duplicate elements and returns a dictionary with
elements as keys and their frequency as values.'''


elements = input("Enter elements separated by spaces: ").split()

frequency_dict = dict()
for item in elements:
    if item in frequency_dict:
        frequency_dict[item] += 1
    else:
        frequency_dict[item] = 1

print("Frequency Dictionary:", frequency_dict)
