'''1. Write a program to take 5 numbers from the user and store them in a tuple, then print the maximum and minimum'''

nums = []

for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    nums.append(num)

num_tuple = tuple(nums)

max_num = num_tuple[0]
min_num = num_tuple[0]

for num in num_tuple:
    if(num > max_num):
        max_num = num
    if(num < min_num):
        min_num = num

print("Tuple:", num_tuple)
print("Maximum Number: ", max_num)
print("Minimum Number: ", min_num)

'''2. Given a tuple of integers, write a program to count how many elements are divisible by 3.'''


input_str = input("Enter numbers separated by spaces: ").strip().split()
nums_tuple = tuple(int(num) for num in input_str if num.strip().isdigit())

count = 0
for num in nums_tuple:
    if num % 3 == 0:
        count += 1

print("Tuple:", nums_tuple)
print("Count of elements divisible by 3:", count)

'''3. Write a program to reverse the contents of a tuple without using reversed().'''


input_str = input("Enter numbers separated by spaces: ").strip().split()
num_tuples = tuple(int(num) for num in input_str if num.strip().isdigit())

reversed_tuple = ()
for i in range(len(num_tuples) - 1, -1, -1):
    reversed_tuple += (num_tuples[i],)

print("Original tuple:", num_tuples)
print("Reversed tuple:", reversed_tuple)

'''-----------------------------------------------------------------------------------------------------------'''