'''1. Check the number for Even or Odd'''
def even_and_odd():
    num = int(input("Enter a number: "))
    if (num % 2 == 0):
        print("Even")
    else:
        print("Odd")




'''2. Password Strength Validator'''
def password_checker():
    password = input("Enter your password: ")

    length = len(password) >= 8
    has_Upper = False
    has_Lower = False
    has_Digit = False
    has_Special = False

    for char in password:
        if (char.isupper):
            has_Upper = True
        elif (char.islower):
            has_Lower = True
        elif (char.isdigit):
            has_Digit = True
        else:
            has_Special = True

    score = sum([length, has_Upper, has_Lower, has_Digit, has_Special])

    if score == 5:
        strength = print("Very Strong")
    elif score == 4:
        strength = print("Strong")
    elif score == 3:
        strength = print("Moderate")
    elif score == 2:
        strength = print("Weak")
    else:
        strength = print("Weak")

    print(f"Password Strength: {strength}")




'''3. Nested Grade Evaluation'''
def grade_evaluation():
    exam_score = float(input("Enter the Exam Score: "))
    attendance = float(input("Enter the Attendance Score: "))

    if(exam_score < 0 or exam_score > 100 or attendance < 0 or attendance > 100):
        print("Invalid Input. Please Enter a Valid Number")
        return
    
    if(exam_score >= 50):
        if(attendance >= 75):
            print("Student Passed")
        else:
            print("Student Failed. Reason: Low Attendance")
    else:
        print("Student Failed. Reason: Low Marks")



'''4. Traffic Fine Calculator'''
def fine_calculator():
    speed_limit = int(input("Enter the Speed Limit: "))
    speed = int(input("Enter the Actual Speed of the Vehicle: "))

    over_speed = speed - speed_limit

    if(over_speed <= 0):
        print("No Fine. You are free to go")
    elif (over_speed <= 10):
        print("Fine: Rs.500")
    elif (over_speed <= 40):
        print("Fine: Rs.1000")
    else:
        print("Fine: Rs.5000 and 2 months Jail")



'''5. Loan Eligibility Checker'''
def loan_eligibility():
    age = int(input("Enter you Age: "))
    income = int(input("Enter your Monthly Income: "))
    credit_score = int(input("Enter you Credit Score: "))

    if(age < 21 or age > 60):
        print("Not Eligible. Age should be between 21 and 60")
    elif(income < 50000):
        print("Income not approved. Loan cannot be granted")
    elif(credit_score < 300 or credit_score > 850):
        print("Invalid Credit Score. Put in a Valid Credit Score")
    elif(credit_score < 650):
        print("Low Credit Score. Loan cannot be granted")
    else:
        print("Loan Approved")

'''Execution'''
even_and_odd()
password_checker()
grade_evaluation()
fine_calculator()
loan_eligibility()