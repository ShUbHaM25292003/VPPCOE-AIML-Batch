'''DAY 1'''

'''1. Write a program that takes the radius as input and calculates the area and
circumference of a circle.'''

pi = 3.1416

radius = float(input("Enter the radius of the circle: "))

area = pi * radius * radius
circumference = 2 * pi * radius

print(f"Area of the Circle is: {area: .2f}")
print(f"Circumference of the Circle is: {circumference: .2f}")

'''2. Write a program to check if a number is divisible by both 3 and 5.'''

num = int(input("Enter a number: "))

if(num % 3 == 0 and num % 5 == 0):
    print("Number is divisible by 3 and 5")
else:
    print("Number is not divisible by 3 and 5")

'''3. Write a program that takes a 4-digit number from the user and prints the sum of its digits.'''

num = input("Enter a 4 digit number: ") 

if(len(num) != 4 or not num.isdigit()):
    print("Please enter a valid four digit number")
else:
    total = 0
    for nums in num:
        total += int(nums)

    print(f"Sum of the digits is: {total}")

'''-------------------------------------------------------------------------------------------------------------'''