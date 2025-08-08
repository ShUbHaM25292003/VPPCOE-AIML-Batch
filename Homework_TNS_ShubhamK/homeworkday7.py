'''1. Write a program that takes a sentence and creates a dictionary with word counts.'''


sentence = input("Enter a sentence: ")

words = sentence.strip().split()

word_count = dict()

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word count dictionary:")
print(word_count)


'''2. Write a program to map roll numbers to names using two lists and form a dictionary.'''


roll_numbers = input("Enter roll numbers separated by spaces: ").strip().split()

names = input("Enter corresponding names separated by spaces: ").strip().split()

if len(roll_numbers) != len(names):
    print("Error: The number of roll numbers and names must be the same.")
else:
    student_dict = dict(zip(roll_numbers, names))
    print("Mapped Dictionary (Roll Number -> Name):")
    print(student_dict)

'''3. Write a program that takes a dictionary of students and their marks, and prints the
name(s) of the student(s) with the highest marks.'''


n = int(input("Enter the number of students: "))

student_marks = dict()

for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    marks = int(input(f"Enter marks of {name}: "))
    student_marks[name] = marks

highest = max(student_marks.values())

top_students = [name for name, mark in student_marks.items() if mark == highest]

print("Student(s) with the highest marks:")
for student in top_students:
    print(student)

'''-----------------------------------------------------------------------------------------------------------'''