'''1. Write a program to find the difference between the maximum and minimum elements in a list'''

nums = input("Enter a list of numbers separated by spaces: ").strip().split()
nums = [int(num) for num in nums if num.strip().isdigit()]

max_num = nums[0]
min_num = nums[0]

for num in nums:
    if (num > max_num):
        max_num = num
    if(num < min_num):
        min_num = num

difference = max_num - min_num

print(f"The difference is: {difference}")


'''2. Write a program to remove all elements at odd indices from a list.'''

nums = input("Enter a list of nums seperated by spaces: ").split()
nums = [int(num) for num in nums]

odd_indice_list = []

for i in range(len(nums)):
    if i % 2 != 0:
        odd_indice_list.append(nums[i])

print(f"List after removing odd indices: {odd_indice_list}")


'''3. Write a program that takes a list of integers and prints only the elements that appear exactly once.'''


nums = input("Enter a list of integers separated by spaces: ").split()
nums = [int(num) for num in nums]

once_an_element = []
for num in nums:
    count = 0
    for other in nums:
        if num == other:
            count += 1
    if count == 1:
        once_an_element.append(num)

print(f"Elements that appear exactly once: {once_an_element}")

'''------------------------------------------------------------------------------------------------------'''