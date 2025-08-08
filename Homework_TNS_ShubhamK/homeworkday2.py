'''DAY 2'''

'''1. Write a program to print the factorial of a number using a for loop'''

num = int(input("Enter a number: "))

if(num < 0):
    print("Please enter a non-negative integer for factorial calculation")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i

    print(f"Factorial of the given number is: {factorial}")


'''2. Write a program that prints all numbers from 1 to 100 that are divisible by 7 but not a
multiple of 5.'''

for nums in range(1, 101):
    if nums % 7 == 0 and nums % 5 != 0:
        print(nums)


'''3. Write a program that takes a number and prints whether it is a palindrome or not.'''

num = input("Enter a number: ")

reverse_num = num[::-1]

if(reverse_num == num):
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")

'''-------------------------------------------------------------------------------------------------------------'''