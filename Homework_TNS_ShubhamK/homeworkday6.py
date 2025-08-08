'''1. Write a program to take two lists from the user and print the common elements using sets.'''

list1 = input("Enter elements of the first list separated by spaces: ").strip().split()
list2 = input("Enter elements of the second list separated by spaces: ").strip().split()

set1 = set(list1)
set2 = set(list2)

common = set1.intersection(set2)

print("Common elements:", list(common))


'''2. Write a program to check if two sets are disjoint or not.'''

sets1 = set(input("Enter elements of the first set separated by spaces: ").strip().split())
sets2 = set(input("Enter elements of the second set separated by spaces: ").strip().split())

if set1.isdisjoint(sets2):
    print("The sets are disjoint (no common elements).")
else:
    print("The sets are NOT disjoint (they share some elements).")


'''3. Write a program to find all unique vowels present in a given string using set.'''

text = input("Enter a string: ").lower()

vowel_set = set('aeiou')

found_vowels = set(text).intersection(vowel_set)

print("Unique vowels found in the string:", list(found_vowels))

'''-------------------------------------------------------------------------------------------------------------'''